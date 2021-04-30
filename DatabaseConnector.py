"""DatabaseConnector 
        * This file contains MyInfluxDBClient class 
        * Usage: Build connection to the InfluxDB server and to a specific database
        * Important settings: influxHost = localhost; port = 8086; other paramters are optional 

    Attributes:
        * name: Sujan Kanapathipillai
        * date: 30.04.2021
        * version: 0.0.1 Beta - free
"""
from influxdb import InfluxDBClient

class MyInfluxDBClient:
    """MyInfluxDBClient
            * Object from this class is needed to interact with the influx database
            * Class holds the connection to the database
    """
    def __init__(self, _influxHost='localhost', _port=8086, _username='admin', _password='Password1', _database='CoronaDB_World_test'):
        """Init for MyInfluxDBClient 
                * Constructor for MyInfluxDBClient

            Args:
                _influxHost (str, optional): Hostname to connect to InfluxDB, defaults to 'localhost'
                _port (int, optional): Port number to connect to InfluxDB, defaults to 8086
                _username (str, optional): User to connect to InfluxDB, defaults to 'admin'
                _password (str, optional): Password of the user, defaults to 'Password1'
                _database (str, optional): Database to which the connection is build, defaults to 'CoronaDB_World_test'
        """
        self.influxHost = _influxHost
        self.port = _port
        self.username = _username
        self.password = _password
        self.database = _database
        self.connection = self.setContoInflux()

    def setContoInflux(self):
        """Set connection to InfluxDB
                * Connection is built to the started InfluxDB server 
                * Try, except block catches occuring errors and gives user messages
        
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed

            Returns:
                client  (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
        
            Test:
                * Could the connection build properly to InfluxDB
        """
        try:
            client = InfluxDBClient(self.influxHost, self.port, self.username, self.password, self.database)
            # Without ping() try, except block does not work
            client.ping()
        except Exception as general_error:
            print("There is a mistake in the arguments of InfluxDBClient: " + str(general_error)) 
            return 
        client.create_database(self.database)
        client.get_list_database()
        client.switch_database(self.database)
        return client



