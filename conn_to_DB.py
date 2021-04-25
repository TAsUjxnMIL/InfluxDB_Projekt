from influxdb import InfluxDBClient

# def set_Con_to_Influx():
#     """set con to influx
#         set connection to Influx database
        
#         Args:
#             none

#         Returns:
#             client  (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
        
#         Test:
#             * is user input correct?
#             * are the default values taken? 
#     """
#     try:
#         client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'CoronaDB_World_test')
#         client.ping()
    
#     except Exception as general_error:
#         print("There is a mistake in the arguments of InfluxDBClient: " + str(general_error)) 
#         return 
    
#     client.create_database('CoronaDB_World_test')
#     client.get_list_database()
#     client.switch_database('CoronaDB_World_test')
#     return client

class MyInfluxDBClient:
    def __init__(self, _localhost='localhost', _port=8086, _username='admin', _password='Password1', _database='CoronaDB_World_test'):
        self.localhost = _localhost
        self.port = _port
        self.username = _username
        self.password = _password
        self.database = _database
        self.connection = self.setContoInflux()

    def setContoInflux(self):
        #Setup database 
        try:
            client = InfluxDBClient(self.localhost, self.port, self.username, self.password, self.database)
            # con = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'CoronaDB') 
            client.ping()
        except Exception as general_error:
            print("There is a mistake in the arguments of InfluxDBClient: " + str(general_error)) 
            return 
        client.create_database('CoronaDB_World_test')
        client.get_list_database()
        client.switch_database('CoronaDB_World_test')
        return client



