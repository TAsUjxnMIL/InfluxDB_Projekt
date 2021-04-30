"""Program start point 
   * Main function where the data analysis is started
   * User is able to choose between multiple functions which can be executed
   
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
import GetDatasets
from KeyValues import KeyPerformanceIndicator


class UnittestClientQueries(unittest.TestCase):
    """These class contains methods with unittests.
       Important to add is that the tests are dependent on the owid-covid-data.csv 
       Trying to change the csv file will end up in failed tests

    Args:
        Testcase (class): With this class single test cases can be instanciated; necessary to do these tests

    TODO Output of the functions should be surpressed when calling from test class 
    """
    def testKPIs(self):
        kpiTester = KeyPerformanceIndicator()
        kpiTester.getAllKPIs()
        actualKPIs = kpiTester.result_numbers
        expectedKPIs = [1305127, 81492, 4474] 
        self.assertEqual(actualKPIs, expectedKPIs)
        print("KPI Test passed successfully!")

    def testWrite(self):
        client = MyInfluxDBClient(_database='CoronaDBTestWriter')
        numberExpectedEntrys = writeToDB(client)
        dbResult = client.connection.query("SELECT COUNT(*) FROM confirmed_cases")
        dbResultList = list(dbResult.get_points())
        numberActualEntrys = dbResultList[0]['count_confirmed']
        self.assertEqual(numberActualEntrys, numberExpectedEntrys)
        print("Writing to database test passed successfully!")

    def testTop(self):
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
        try:
            client = InfluxDBClient(host='localhost', port=8086, username='admin', database='CoronaDBTestConnection')  
            client.ping()
        except Exception as conError:
            print("Something went wrong: " + str(conError))
        client.create_database('CoronaDBTestConnection')
        client.get_list_database()
        client.switch_database('CoronaDBTestConnection')
        print("Connection test passed successfully!")
 
    def run(self):
        self.testKPIs()
        self.testWrite()
        self.testTop()
        self.testFlop()
        self.testConnection
        




