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
from conn_to_DB import MyInfluxDBClient

if __name__ == '__main__':
    # routine here 
    client = MyInfluxDBClient()
    
    if not client.connection.query("SELECT COUNT(*) FROM /.*/"):
        print("Database is empty. Wait a few seconds data will be written on database in seconds!\n")
        write_to_DB.readDataFromCSV(client)       

    #get_data_DB.get_top_flop(client, "TOP")
    #get_data_DB.get_all_data(client)
    #get_data_DB.get_KPIs(client)







