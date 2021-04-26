import pandas as pd 
from datetime import datetime
import conn_to_DB as con

def readDataFromCSV(client):
    """read data from csv
        Data is read from .csv file, after this data is written on database

    Args:
        client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object

    Return:
        none 

    Test:
        *
    
    TODO Write only data from 2021 to database
    """
    # path variable 
    file_path = 'C:\\Users\\sujan\\Documents\\Duales Studium\\Theorie\\4.Semester\\Grundlagen der Datenbanken\\InfluxDB_Projekt\\Time_Series_Corona_Data\\owid-covid-data.csv'
    # Read the data into csvReader 
    csvReader = pd.read_csv(file_path)
    # Set variables 
    date = csvReader.date
    #tags = csvReader.iso_code
    state = csvReader.location.str.replace(" ", "_", case=False) #tag should not contain blank spaces
    vaccinated = csvReader.new_vaccinations
    confirmed = csvReader.new_cases
    deaths = csvReader.new_deaths

      
    #Setup Payload 
    json_payload = []
    for i in range(1, len(csvReader)):
        confirmed_json = {
            "measurement": "confirmed_cases",
            "tags":{
                "location": state[i]
            },
            "time": date[i],
            "fields":{
                'confirmed': confirmed[i]
            }
        }
  
        death_json = {
            "measurement": "death_cases",
            "tags":{
                "location": state[i]
            },
            "time": date[i],
            "fields":{
                'deaths': deaths[i]
            }
        }

        vaccinated_json = {
            "measurement": "vaccinated_person",
            "tags":{
                "location": state[i]
            },
            "time": date[i],
            "fields":{
                'vaccinated': vaccinated[i]
            }
        }


        json_payload.append(confirmed_json)
        json_payload.append(death_json)
        json_payload.append(vaccinated_json)
    _ = client.connection.write_points(json_payload)