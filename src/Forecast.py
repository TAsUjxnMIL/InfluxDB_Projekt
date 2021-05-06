"""Forecast 
   * Forecast algorithm fbprophet from facebook
   * Number of vaccinated persons are predicted 
   
   Attributes:
        name: Sujan Kanapathipillai
        date: 30.04.2021
        version: 0.0.1 Beta - free
         
"""
from pandas import DataFrame
import pandas as pd
from datetime import datetime
from fbprophet import Prophet 
from fbprophet.plot import plot
import matplotlib.pyplot as plt
from ResponseConverterDF import ResponseConverterDF
from DatabaseWriter import writeToDBForecast


def forecast(client, country):
    """Prophet forecast algorithm
            * Prophet gets data that is written in resultsVaccinatedDF and calculates forcasted data for the next 50 days
            * Prophet needs the data in specific column names ds and y without the algorithm does not work 

        Args:
            client  (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
            country (string): User input to change the select query, incorrect input --> exception
    
        Return:
            none
    
        datetime:
            * Is the user input correct? 
        TODO Ask user if he wants to write the data on database
        TODO Delete country in query 
    """
    converterDF = ResponseConverterDF()
    try:
        resultsVaccinatedDF = converterDF.responseConversion(f"SELECT vaccinated FROM vaccinated_cases \
                                WHERE location='{country}' ORDER BY time DESC", client) 
        resultsVaccinatedDF.columns = ['ds', 'y']
    except ValueError as valError:
        print("There is a mistake in the query, so no response. " + str(valError))
        return
    # Changing the date format, needed for prediction with fbprophet 
    resultsVaccinatedDF["ds"] = pd.to_datetime(resultsVaccinatedDF["ds"]).dt.date
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    model.fit(resultsVaccinatedDF)
    future = model.make_future_dataframe(periods=50)
    forecast = model.predict(future)
    model.plot(forecast)
    plt.show()

    writeToDBForecast(client, forecast, country, resultsVaccinatedDF["ds"])

   

