import pandas as pd 
from datetime import datetime
import conn_to_DB as con



def readDataFromCSV():
    # path variable 
    file_path = 'C:\\Users\\sujan\\Documents\\Duales Studium\\Theorie\\4.Semester\\Grundlagen der Datenbanken\\Projekt_TimeSeriesData\\covid_19_india.csv'
    # Read the data into csvReader 
    csvReader = pd.read_csv(file_path)
    # Set variables 
    date = csvReader.Date
    time = csvReader.Time
    datetime = date + " " + time  
    tags = csvReader.Sno
    state = csvReader["State/UnionTerritory"].str.replace(" ", "_", case=False) #tag should not contain blank spaces
    confirmed = csvReader.Confirmed
    cured = csvReader.Cured
    deaths = csvReader.Deaths

      
    #Setup Payload 
    json_payload = []
    for i in range(1, len(csvReader)):
        confirmed_json = {
            "measurement": "confirmed_cases",
            "tags":{
                "SerialNumber": tags[i],
                "location": state[i]
            },
            "time": datetime[i],
            "fields":{
                'Confirmed': confirmed[i]
            }
        }
  
        death_json = {
            "measurement": "death_cases",
            "tags":{
                "SerialNumber": tags[i],
                "location": state[i]
            },
            "time": datetime[i],
            "fields":{
                'Deaths': deaths[i]
            }
        }

        cured_json = {
            "measurement": "cured_cases",
            "tags":{
                "SerialNumber": tags[i],
                "location": state[i]
            },
            "time": datetime[i],
            "fields":{
                'Cured': cured[i]
            }
        }


        json_payload.append(confirmed_json)
        json_payload.append(death_json)
        json_payload.append(cured_json)
        client = con.setContoInflux()
    _ = client.write_points(json_payload)
