"""Get datasets from InfluxDb
   * This file contains those functions that read datasets from the InfluxDB 
   * These datasets are plotted afterwards
   * Important: More than 80.000 entries are plotted, it could take a bit longer 
   
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

def getTopFlop(client, choice, terminalOutput=True):
    """Get top flop 
            * Get 10 countries with the highest/lowest number of confirmed cases
            TODO user should decide if he wants to see confirmed, vaccinated, death
        
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
    if terminalOutput:
        print(dfTopFlop)
    return dfTopFlop 

def getAllData(client, plotFlag):
    
    """Get all data 
            * All confirmed/vaccinated/death cases are read out from the database, the data is compared and plotted

        Args:
            client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
            plotFlag (int): Contains user choice, which overview shall be shown

        Return:
            none
    """
    converterDF = ResponseConverterDF()

    resultConfirmed = converterDF.responseConversion("SELECT * FROM confirmed_cases", client)
    resultConfirmed.columns = ['Date', 'Confirmed Cases', 'State']
    resultConfirmed["Date"] = pd.to_datetime(resultConfirmed["Date"]).dt.date

    resultDeath = converterDF.responseConversion("SELECT * FROM death_cases", client)
    resultDeath.columns = ['Date', 'Death Cases', 'State']
    resultDeath["Date"] = pd.to_datetime(resultDeath["Date"]).dt.date

    resultVaccinated = converterDF.responseConversion("SELECT * FROM vaccinated_cases", client)
    resultVaccinated.columns = ['Date', 'State', 'Vaccinated Person']
    resultVaccinated["Date"] = pd.to_datetime(resultVaccinated["Date"]).dt.date

    if plotFlag == 1:
        plotBarChart(resultConfirmed, resultDeath, resultVaccinated)
    elif plotFlag == 2:
        showTreeMap(resultConfirmed, resultDeath, resultVaccinated)
    else:
        plotBarChart(resultConfirmed, resultDeath, resultVaccinated)
        showTreeMap(resultConfirmed, resultDeath, resultVaccinated)
        
def plotBarChart(resultConfirmed, resultDeath, resultVaccinated):
    """Plot Bar Chart
            * Data from getAllData function is plotted here with matplotlib.pyplot

    Args:
        resultConfirmed (DataFrame): Confirmed cases during pandamic - data from database
        resultDeath (DataFrame): Death cases during pandamic - data from database
        resultVaccinated (DataFrame): Vaccinated cases during pandamic - data from database
    
    Return: 
        none
    """
    fig, ax = plt.subplots(3)

    ax[0].plot(resultConfirmed['Date'], resultConfirmed['Confirmed Cases'])
    ax[0].title.set_text('Confirmed Cases')
    
    ax[1].plot(resultDeath['Date'], resultDeath['Death Cases'])
    ax[1].title.set_text('Death Cases')
    
    ax[2].plot(resultVaccinated['Date'], resultVaccinated['Vaccinated Person'])
    ax[2].title.set_text('Vaccinated Cases')
    fig.tight_layout()
    plt.show()

def showTreeMap(resultConfirmed, resultDeath, resultVaccinated):
    """Show treemap
            * Data from getAllData function is shown in a treemap within the browser (browser opens automatically)

    Args:
        resultConfirmed (DataFrame): Confirmed cases during pandamic - data from database
        resultDeath (DataFrame): Death cases during pandamic - data from database
        resultVaccinated (DataFrame): Vaccinated cases during pandamic - data from database

    Return: 
        none
    """
    figVaccinated = px.treemap(resultVaccinated, path=['State'], values='Vaccinated Person', title='Cured Cases State Comparison')
    figVaccinated.show()
    figDeath = px.treemap(resultDeath, path=['State'], values='Death Cases', title='Death Cases State Comparison')
    figDeath.show()
    figConfirmed = px.treemap(resultConfirmed, path=['State'], values='Confirmed Cases', title='Vaccinated person State Comparison')
    figConfirmed.show()