"""Program start point 
   * Main function where the data analysis is started
   * User is able to choose between multiple functions which can be executed
   
   Attributes:
        name: Sujan Kanapathipillai
        date: 30.04.2021
        version: 0.0.1 Beta - free
"""
import matplotlib.pyplot as plt 
import plotly.express as px
from pandas import DataFrame
import pandas as pd
import numpy as np
from ResponseConverterDF import ResponseConverterDF

def getTopFlop(client, choice):
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
    converterDF = ResponseConverterDF()
    dfTopFlop = converterDF.responseConversion(f'SELECT {choice}("confirmed", 1), "location"::tag \
     FROM "confirmed_cases" GROUP BY location ORDER BY time', client)
    # Create dataframe to show table in the terminal
    dfTopFlop.columns = ['Date', 'Confirmed Cases', 'State']
    dfTopFlop = dfTopFlop.astype({'Confirmed Cases':int})
    # Edit for terminal output
    dfTopFlop = dfTopFlop.sort_values(by=['Confirmed Cases'])
    dfTopFlop = dfTopFlop.iloc[::-1]
    dfTopFlop = dfTopFlop.iloc[0:5, :]
    dfTopFlop = dfTopFlop.reset_index(drop=True)
    print(dfTopFlop)
    return dfTopFlop 


def getAllData(client):
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
    converterDF = ResponseConverterDF()
    fig, ax = plt.subplots(3)
    
    resultConfirmed = converterDF.responseConversion("SELECT * FROM confirmed_cases", client)
    resultConfirmed.columns = ['Date', 'Confirmed Cases', 'State']
    resultConfirmed["Date"] = pd.to_datetime(resultConfirmed["Date"]).dt.date
    ax[0].plot(resultConfirmed['Date'], resultConfirmed['Confirmed Cases'])
    ax[0].title.set_text('Confirmed Cases')
    
    resultDeath = converterDF.responseConversion("SELECT * FROM death_cases", client)
    resultDeath.columns = ['Date', 'Death Cases', 'State']
    resultDeath["Date"] = pd.to_datetime(resultDeath["Date"]).dt.date
    ax[1].plot(resultDeath['Date'], resultDeath['Death Cases'])
    ax[1].title.set_text('Death Cases')
    
    resultVaccinated = converterDF.responseConversion("SELECT * FROM vaccinated_cases", client)
    resultVaccinated.columns = ['Date', 'State', 'Vaccinated Person']
    resultVaccinated["Date"] = pd.to_datetime(resultVaccinated["Date"]).dt.date
    ax[2].plot(resultVaccinated['Date'], resultVaccinated['Vaccinated Person'])
    ax[2].title.set_text('Vaccinated Cases')
    fig.tight_layout()
    plt.show()

    fig1 = px.treemap(resultVaccinated, path=['State'], values='Vaccinated Person', title='Cured Cases State Comparison')
    fig1.show()
    fig2 = px.treemap(resultDeath, path=['State'], values='Death Cases', title='Death Cases State Comparison')
    fig2.show()
    fig3 = px.treemap(resultConfirmed, path=['State'], values='Confirmed Cases', title='Vaccinated person State Comparison')
    fig3.show()


    