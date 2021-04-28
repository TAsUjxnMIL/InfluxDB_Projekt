from pandas import DataFrame
import pandas as pd
from fbprophet import Prophet 
from fbprophet.plot import plot
import matplotlib.pyplot as plt
from convert_DB_response import response_Conversion


def prophet_forecast(client, country):
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
    try:
        df_results_vaccinated = response_Conversion(f"SELECT confirmed FROM confirmed_cases WHERE location='{country}' ORDER BY time DESC", client)
        # Changing column names. Needed for prediction with fbprophet 
        df_results_vaccinated.columns = ['ds', 'y']
    except ValueError as val_error:
        print("There is a mistake in the query, so no response. " + str(val_error))
        return
    # Changing the date format, needed for prediction with fbprophet 
    df_results_vaccinated["ds"] = pd.to_datetime(df_results_vaccinated["ds"]).dt.date
    # for i in range(0, len(df_results_vaccinated)):
    #     df_results_vaccinated['ds'][i] =  df_results_vaccinated['ds'][i].replace("T00:00:00Z", "")
    # Instanciating Prophet object
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    model.fit(df_results_vaccinated)
    # Prediction for the next 365 days
    future = model.make_future_dataframe(periods=50)
    forecast = model.predict(future)
    model.plot(forecast)
    plt.show()