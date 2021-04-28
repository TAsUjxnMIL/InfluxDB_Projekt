import matplotlib.pyplot as plt 
import plotly.express as px
from pandas import DataFrame
import pandas as pd
import numpy as np
from convert_DB_response import response_Conversion

def get_top_flop(client, choice):
    """get top flop 
        Get 10 countries with the highest/lowest number of vaccinated/deaths/confirmed cases
        
        Args:
            client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
            choice (string): user can decide between top/ flop cases

        Return:
            none
        
        Test:
            * Is the user input a string?
            * Is the user input correct? 
    """
    df_top_flop = response_Conversion(f'SELECT {choice}("confirmed", 1), "location"::tag FROM "confirmed_cases" GROUP BY location ORDER BY time', client)
    # Create dataframe to show table in the terminal
    df_top_flop.columns = ['Date', 'Confirmed Cases', 'State']
    df_top_flop = df_top_flop.astype({'Confirmed Cases':int})
    # Edit for terminal output
    df_top_flop = df_top_flop.sort_values(by=['Confirmed Cases'])
    df_top_flop = df_top_flop.iloc[::-1]
    df_top_flop = df_top_flop.iloc[0:5, :]
    df_top_flop = df_top_flop.reset_index(drop=True)
    print(df_top_flop)
    return df_top_flop 


def get_all_data(client):
    """get all data 
        All confirmed/vaccinated/death cases are read out from the database, the data is compared and plotted

    Args:
        client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object

    Return:
        none

    Test:
        * do the plots appear?
        * browser opened with treemap?

    TODO Maybe outsource the treemap
    """
    fig, ax = plt.subplots(3)
    
    result_confirmed = DataFrame(list(client.connection.query("SELECT * FROM confirmed_cases").get_points()))
    result_confirmed.columns = ['Date', 'Confirmed Cases', 'State']
    result_confirmed["Date"] = pd.to_datetime(result_confirmed["Date"]).dt.date
    ax[0].plot(result_confirmed['Date'], result_confirmed['Confirmed Cases'])
    ax[0].title.set_text('Confirmed Cases')
    
    result_death = DataFrame(list(client.connection.query("SELECT * FROM death_cases").get_points()))
    result_death.columns = ['Date', 'Death Cases', 'State']
    result_death["Date"] = pd.to_datetime(result_death["Date"]).dt.date
    ax[1].plot(result_death['Date'], result_death['Death Cases'])
    ax[1].title.set_text('Death Cases')
    
    result_vaccinated = DataFrame(list(client.connection.query("SELECT * FROM vaccinated_cases").get_points()))
    result_vaccinated.columns = ['Date', 'State', 'Vaccinated Person']
    result_vaccinated["Date"] = pd.to_datetime(result_vaccinated["Date"]).dt.date
    ax[2].plot(result_vaccinated['Date'], result_vaccinated['Vaccinated Person'])
    ax[2].title.set_text('Vaccinated Cases')
    fig.tight_layout()
    plt.show()

    fig1 = px.treemap(result_vaccinated, path=['State'], values='Vaccinated Person', title='Cured Cases State Comparison')
    fig1.show()
    fig2 = px.treemap(result_death, path=['State'], values='Death Cases', title='Death Cases State Comparison')
    fig2.show()
    fig3 = px.treemap(result_confirmed, path=['State'], values='Confirmed Cases', title='Vaccinated person State Comparison')
    fig3.show()


    