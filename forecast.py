from pandas import DataFrame
from fbprophet import Prophet 
from fbprophet.plot import plot


def prophet_forecast(client):
    """[summary]

    Args:
        client ([type]): [description]
        
    # TODO Import the newly predicted data for the next year to the database 
    # TODO Plot the predicted data 
    """
    results_vaccinated = client.connection.query("SELECT confirmed FROM confirmed_cases ORDER BY time DESC")
    results_vaccinated = results_vaccinated.get_points()
    results_vaccinated = list(results_vaccinated)
    df_results_vaccinated = DataFrame(results_vaccinated)
    # Changing column names. Needed for prediction with fbprophet 
    df_results_vaccinated.columns = ['ds', 'y']
    # Changing the date format, needed for prediction with fbprophet 
    for i in range(0, len(df_results_vaccinated)):
        df_results_vaccinated['ds'][i] =  df_results_vaccinated['ds'][i].replace("T00:00:00Z", "")
    # Instanciating Prophet object
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    model.fit(df_results_vaccinated)
    # Prediction for the next 365 days
    future = model.make_future_dataframe(periods=365)
    forecast = model.predict(future)

    

    