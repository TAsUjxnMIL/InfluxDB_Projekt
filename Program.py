"""Start point InfluxDB program

    tipp:
        Ensure that you start the InfluxDB server in a terminal 
    attributes:
        name: Sujan Kanapathipillai
        date: 25.04.2021
        version: 0.0.1
"""
import write_to_DB
import conn_to_DB
import get_data_DB
import unittest
from conn_to_DB import MyInfluxDBClient
from forecast import prophet_forecast

if __name__ == '__main__':
    # routine here 
    client = MyInfluxDBClient()
    if not client.connection.query("SELECT COUNT(*) FROM /.*/"):
        print("Database is empty. Wait a few seconds data will be written on database in seconds!\n")
        write_to_DB.readDataFromCSV(client)   
    
    print("(a) - Top/Flop 10 countries with the highest number of cases")
    print("(b) - Compare Confirmed, Death, Vaccinated Cases in a plot")
    print("(c) - Get Key Performance Indicators")
    print("(d) - Get a prediction how the incidents will develop in the next 100 days")
    choice = input("Enter your choice: \n")
    print(type(choice))
    print(choice)

    if choice == 'a':
        print("Do you want the Top(1) or Flop(2) countries")
        choice_countries = input("Enter the number: ")
        if choice_countries == '1':
            _ = get_data_DB.get_top_flop(client, "TOP")
        elif choice_countries == '2':
            _ = get_data_DB.get_top_flop(client, "BOTTOM")

    elif choice == 'b':
        get_data_DB.get_all_data(client)

    elif choice == 'c':
        _ = get_data_DB.get_KPIs(client)
    
    elif choice == 'd':
        prophet_forecast(client)    






