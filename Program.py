import write_to_DB
import conn_to_DB

if __name__ == '__main__':
    client = conn_to_DB.setContoInflux()
    write_to_DB.readDataFromCSV()


    # TODO actual field set has to be split up into 5 measurements --> Time stamp is always the same 
    # The location (State/UnionTerritory) could be a tag for confirmed; deaths; confirmed 
    # Serial number (Sno) could be the tag for all measurements(look at current fields)






