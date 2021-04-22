from influxdb import InfluxDBClient

def setContoInflux():
    #Setup database 
    client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'CoronaDB_test1')
    client.create_database('CoronaDB_test1')
    client.get_list_database()
    client.switch_database('CoronaDB_test1')
    return client
