"""Unittests 
   * File contains all Client and query unittests  
   
   Attributes:
        name: Sujan Kanapathipillai
        date: 30.04.2021
        version: 0.0.1 Beta - free 
"""
import unittest
import pandas as pd
import pandas.testing as pd_testing
from DatabaseWriter import writeToDB
from influxdb import InfluxDBClient
from DatabaseConnector import MyInfluxDBClient
from KeyValues import KeyPerformanceIndicator
import GetDatasets



class UnittestClientQueries(unittest.TestCase):
    """These class contains methods with unittests.
       Important to add is that the tests are dependent on the owid-covid-data.csv 
       Trying to change the csv file will end up in failed tests

    Args:
        Testcase (class): With this class single test cases can be instanciated; necessary to do these tests

    TODO Output of the functions should be surpressed when calling from test class 
    """
    def testKPIs(self):
        """Test KPIs
                * The Key values returned by the methods in KeyValues.py are always the same for the owid-covid-data.csv file
                  So the values can be hardcoded in expectedKPIs and afterwards compared to actualKPIs
                * actualKPIs holds the real values from the database (kpi.Tester reads the data from influxDB)
        """
        kpiTester = KeyPerformanceIndicator()
        kpiTester.getAllKPIs()
        actualKPIs = kpiTester.resultNumbers
        expectedKPIs = [1305127, 81492, 4474] 
        self.assertEqual(actualKPIs, expectedKPIs)
        print("KPI Test passed successfully!")

    def testTop(self):
        """Test Top
                * This test function tests the getTopFlop function within GetDatasets
                * The function call contains the argument "TOP" to get the top countries from database
                * expectedDFtop contains the values as a dataframe that should be read from the database
        """
        client = MyInfluxDBClient()
        actualDFtop = GetDatasets.getTopFlop(client, "TOP")
        expectedDFtop = pd.DataFrame({
            'Date':[
                '2021-04-22T22:00:00Z',
                '2021-01-01T23:00:00Z',
                '2021-04-10T22:00:00Z',
                '2021-03-24T23:00:00Z',
                '2021-01-24T23:00:00Z'
            ],
            'Confirmed Cases':[
                346786,
                300310,
                117900,
                100158,
                93822
            ],
            'State':[
                'India',
                'United_States',
                'France',
                'Brazil',
                'Spain'
            ]
        })
        expectedDFtop['Confirmed Cases'] = expectedDFtop['Confirmed Cases'].astype("int32")
        pd_testing.assert_frame_equal(actualDFtop, expectedDFtop)
        print("Get top corona cases test passed successfully!")
        
    def testFlop(self):
        """Test Flop
                * This test function tests the getTopFlop function within GetDatasets
                * The function call contains the argument "BOTTOM" to get the flop countries from database
                * expectedDFflop contains the values as a dataframe that should be read from the database
        """
        client = MyInfluxDBClient()
        actualDFflop = GetDatasets.getTopFlop(client, "BOTTOM")
        expectedDFflop = pd.DataFrame({
            'Date':[
                '2020-02-18T23:00:00Z',
                '2020-03-26T23:00:00Z',
                '2020-03-20T23:00:00Z',
                '2020-03-13T23:00:00Z',
                '2021-01-23T23:00:00Z'
            ],
            'Confirmed Cases':[
                2,
                0,
                0,
                0,
                0
            ],
            'State':[
                'Iran',
                'Laos',
                'Haiti',
                'Guinea',
                'Guernsey'
            ]
        })
        expectedDFflop['Confirmed Cases'] = expectedDFflop['Confirmed Cases'].astype("int32")
        pd_testing.assert_frame_equal(actualDFflop, expectedDFflop)
        print("Get flop corona cases test passed successfully!")

    def testConnection(self):
        """Test Connection
                * This function tests the database connection 
        """
        try:
            client = InfluxDBClient(host='localhost', port=8086, username='admin', database='CoronaDBTestConnection')  
            client.ping()
        except Exception as conError:
            print("Connection test failed: " + str(conError))
        client.create_database('CoronaDBTestConnection')
        client.get_list_database()
        client.switch_database('CoronaDBTestConnection')
        print("Connection test passed successfully!")
 
    def testWrite(self):
        """Test Write
                * This test function tests if the writeToDB function works properly
                * Test passes if the number of entries in the owid-covid-data.csv equals the number of entries in the database,
                  That means all the data from the .csv could be written properly
                * Important: SELECT COUNT(*) FROM confirmed_cases returns the total amount of rows from measurement confirmed_cases
                             this is the same as the total number of entries (because of column wise data in .csv file)
        """
        client = MyInfluxDBClient(_database='CoronaDBTestWriter')
        numberExpectedEntrys = writeToDB(client)
        dbResult = client.connection.query("SELECT COUNT(*) FROM confirmed_cases")
        dbResultList = list(dbResult.get_points())
        numberActualEntrys = dbResultList[0]['count_confirmed']
        self.assertEqual(numberActualEntrys, numberExpectedEntrys)
        print("Writing to database test passed successfully!")

    def run(self):
        """Run 
                * This function is called from the main starting point
                * It calls all test functions within this Unittest.py file
        """
        self.testKPIs()
        self.testWrite()
        self.testTop()
        self.testFlop()
        self.testConnection()
        




