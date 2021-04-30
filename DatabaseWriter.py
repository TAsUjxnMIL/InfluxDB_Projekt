import pandas as pd 
from datetime import datetime
from pandas import DataFrame

def writeToDB(client):
    """write data to influxDB
    Data from .csv is read an saved into the df_csv dataframe.
    Important columns from csv are saved into variables.
    Within for loop lists are filles which are imported to influxDB

    Args:
        client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
    
    Return:
        None
    """
    file_path = 'Time_Series_Corona_Data/owid-covid-data.csv'
    df_csv = pd.read_csv(file_path)
    # Change all occurences of nan to 0. Without rows are deleted automatically
    df_csv.fillna(0, inplace=True)
    confirmed_measurement = []
    vaccinated_measurement = []
    death_measurement = []

    # Tag should not contain blank spaces
    state = df_csv.location.str.replace(" ", "_", case=False) 
    date = df_csv.date
    vaccinated = df_csv.new_vaccinations
    confirmed = df_csv.new_cases
    deaths = df_csv.new_deaths

    for i in range(0, len(df_csv)):
        timestamp = int(datetime.strptime(date[i], "%Y-%m-%d").timestamp())
        confirmed_measurement.append(f"confirmed_cases,location={state[i]} confirmed={confirmed[i]} {timestamp}")
        death_measurement.append(f"death_cases,location={state[i]} deaths={deaths[i]} {timestamp}")
        vaccinated_measurement.append(f"vaccinated_cases,location={state[i]} vaccinated={vaccinated[i]} {timestamp}")
    # All measurements cannot be imported at once-->multiple calls
    _ = client.connection.write_points(confirmed_measurement, protocol='line',time_precision='s')
    _ = client.connection.write_points(death_measurement, protocol='line',time_precision='s')
    _ = client.connection.write_points(vaccinated_measurement, protocol='line', time_precision='s')

    
   

    return len(df_csv)

