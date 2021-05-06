"""DatabaseWriter
        * This file contains the writeToDb function which writes data from .csv to the influxDB 
        * Invoked at the first time when database is empty and for the unittest
        * Important: Reading from .csv and writing to database is adapted to the owid-covid-data.csv
          -->Exchange of .csv file is not intended!

    Attributes:
        * name: Sujan Kanapathipillai
        * date: 30.04.2021
        * version: 0.0.1 Beta - free
"""
import pandas as pd 
from datetime import datetime
from pandas import DataFrame

def writeToDB(client):
    """write data to influxDB
    Data from .csv is read an saved into the dfCSV dataframe.
    Important columns from csv are saved into variables.
    Within for loop lists are filles which are imported to influxDB

    Args:
        client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
    
    Return:
        len(dfCSV) (int): The number of entries in the database for the unittests
    """
    filePath = 'data/owid-covid-data.csv'
    dfCSV = pd.read_csv(filePath)
    # Change all occurences of nan to 0. Without rows are deleted automatically
    dfCSV.fillna(0, inplace=True)
    confirmedMeasurement = []
    vaccinatedMeasurement = []
    death_measurement = [] 

    # Tag within influxDB should not contain blank spaces
    state = dfCSV.location.str.replace(" ", "_", case=False) 
    date = dfCSV.date
    vaccinated = dfCSV.new_vaccinations
    confirmed = dfCSV.new_cases
    deaths = dfCSV.new_deaths

    for i in range(0, len(dfCSV)):
        timestamp = int(datetime.strptime(date[i], "%Y-%m-%d").timestamp())
        confirmedMeasurement.append(f"confirmed_cases,location={state[i]} confirmed={confirmed[i]} {timestamp}")
        death_measurement.append(f"death_cases,location={state[i]} deaths={deaths[i]} {timestamp}")
        vaccinatedMeasurement.append(f"vaccinated_cases,location={state[i]} vaccinated={vaccinated[i]} {timestamp}")
    # All measurements cannot be imported at once-->multiple calls
    _ = client.connection.write_points(confirmedMeasurement, protocol='line',time_precision='s')
    _ = client.connection.write_points(death_measurement, protocol='line',time_precision='s')
    _ = client.connection.write_points(vaccinatedMeasurement, protocol='line', time_precision='s')

    return len(dfCSV)

def writeToDBForecast(client, forecast, country, resultsVaccinatedDF):
    expectedMeasurement = []
    trendMeasurement = []
    weeklyMeasurement = []
    timestamp = pd.to_datetime(forecast['ds'], unit='s')
    timestamp = pd.to_datetime(resultsVaccinatedDF).dt.date
    for i in range(0, len(timestamp)):
        date = int(datetime.strptime(str(timestamp[i]), "%Y-%m-%d").timestamp())
        expectedMeasurement.append(f"expected_vaccinations,location={country} ex_vaccinations={forecast['yhat'][i]} {date}")
        trendMeasurement.append(f"trend_vaccinations,location={country} tr_vaccinations={forecast['trend'][i]} {date}")
        weeklyMeasurement.append(f"weekly_vaccinations,location={country} we_vaccinations={forecast['weekly'][i]} {date}")

    try:
        _ = client.connection.write_points(expectedMeasurement, protocol='line',time_precision='s')
        _ = client.connection.write_points(trendMeasurement, protocol='line',time_precision='s')
        _ = client.connection.write_points(weeklyMeasurement, protocol='line', time_precision='s')  
    except Exception as writeError:
        print("There is a mistake in writing on the database: " + str(writeError))
        return 
    print("Predicted data is now on the database!")