"""Program start point 
   * Main function where the data analysis is started
   * User is able to choose between multiple functions which can be executed
   
   Reminder:
        * Ensure that you start the InfluxDB server in a terminal 
   Attributes:
        name: Sujan Kanapathipillai
        date: 30.04.2021
        version: 0.0.1 Beta - free
        
        TODO think of change the switch case into objectoriented 
"""
from DatabaseWriter import writeToDB
from DatabaseConnector import MyInfluxDBClient
from Unittests import UnittestClientQueries
from KeyValues import KeyPerformanceIndicator
import GetDatasets
from Forecast import forecast
import time

if __name__ == '__main__':
    # routine here 
    client = MyInfluxDBClient()
    if not client.connection.query("SELECT COUNT(*) FROM /.*/"):
        print("Database is empty. Wait a few seconds data will be written on database in seconds!\n")
        _ = writeToDB(client)   

    # Terminal menu
    while True:
        print("(a) - Top/Flop 10 countries with the highest number of cases")
        print("(b) - Compare Confirmed, Death, Vaccinated Cases in a plot")
        print("(c) - Get Key Performance Indicators")
        print("(d) - Get a prediction how the incidents will develop in the next 100 days")
        print("(X) - To run unittest and afterwards exit program press another button")
        choice = input("Enter your choice: ")

        if choice == 'a':
            print("Do you want the Top(1) or Flop(2) countries")
            choiceContry = input("Enter the number: ")
            if choiceContry == '1':
                _ = GetDatasets.getTopFlop(client, "TOP")
            elif choiceContry == '2':
                _ = GetDatasets.getTopFlop(client, "BOTTOM")

        elif choice == 'b':
            plotFlag = input("Do you want to see a common plot(1), treemap(2), both(random number): ")
            GetDatasets.getAllData(client, int(plotFlag))

        elif choice == 'c':
            kpiGetter = KeyPerformanceIndicator()
            kpiGetter.getAllKPIs()
        
        elif choice == 'd':
            country = input("Enter the country from which you want the predicted data from (See countryNames.txt):\n")
            forecast(client, country)
        else:
            myUnittests = UnittestClientQueries()
            myUnittests.run()
            exit()

