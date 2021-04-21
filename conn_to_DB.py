from influxdb import InfluxDBClient

def setContoInflux():
    #Setup database 
    client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'CoronaDB_test')
    client.create_database('CoronaDB_test')
    client.get_list_database()
    client.switch_database('CoronaDB_test')
    return client
