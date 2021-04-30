"""Program start point 
   * Main function where the data analysis is started
   * User is able to choose between multiple functions which can be executed
   
   Attributes:
        name: Sujan Kanapathipillai
        date: 30.04.2021
        version: 0.0.1 Beta - free
         
"""
from pandas import DataFrame
import pandas as pd
from fbprophet import Prophet 
from fbprophet.plot import plot
import matplotlib.pyplot as plt
from ResponseConverterDF import ResponseConverterDF


def forecast(client, country):
    """Prophet forecast algorithm
        Prophet gets data that is written in results_vaccinted and calculates forcasted data for the next 50 days

    Args:
        client  (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
        country (string): User input to change the select query
    
    Return:
        none
    
    Test:
        * Is the user input correct?
        
    # TODO Import the newly predicted data for the next year to the database 
    """
    converterDF = ResponseConverterDF()
    try:
        resultsConfirmedDF = converterDF.responseConversion(f"SELECT confirmed FROM confirmed_cases \
                                WHERE location='{country}' ORDER BY time DESC", client)
        # Changing column names. Needed for prediction with fbprophet 
        resultsConfirmedDF.columns = ['ds', 'y']
    except ValueError as valError:
        print("There is a mistake in the query, so no response. " + str(valError))
        return
    # Changing the date format, needed for prediction with fbprophet 
    resultsConfirmedDF["ds"] = pd.to_datetime(resultsConfirmedDF["ds"]).dt.date
    # Instanciating Prophet object
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    model.fit(resultsConfirmedDF)
    # Prediction for the next 365 days
    future = model.make_future_dataframe(periods=50)
    forecast = model.predict(future)
    model.plot(forecast)
    plt.show()