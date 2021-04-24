import write_to_DB
from conn_to_DB import MyInfluxDBClient
import get_data_DB

if __name__ == '__main__':
    client = MyInfluxDBClient()
    #client = conn_to_DB.setContoInflux()
    # write_to_DB.readDataFromCSV(client)
    #get_data_DB.get_top_flop_cured(client, "TOP")
    #get_data_DB.get_all_data(client)
    get_data_DB.get_KPIs(client)







