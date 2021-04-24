from influxdb import InfluxDBClient


class MyInfluxDBClient:
    def __init__(self, _localhost='localhost', _port=8068, _username='admin', _password='Password1', _database='CoronaDB'):
        self.localhost = _localhost
        self.port = _port
        self.username = _username
        self.password = _password
        self.database = _database
        self.connection = self.setContoInflux()

    def setContoInflux(self):
        #Setup database 
        try:
            #con = InfluxDBClient(self.localhost, self.port, self.username, self.password, self.database)
            con = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'CoronaDB') 
            con.ping()
        except Exception as general_error:
            print("There is a mistake in the arguments of InfluxDBClient: " + str(general_error)) 
            return 
        con.create_database('CoronaDB')
        con.get_list_database()
        con.switch_database('CoronaDB')
        return con
