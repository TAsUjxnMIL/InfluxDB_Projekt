import matplotlib.pyplot as plt 
import plotly.express as px
from pandas import DataFrame

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
    result = client.connection.query(f'SELECT {choice}("confirmed", 1), "location"::tag FROM "confirmed_cases" GROUP BY location ORDER BY time')
    # Return value is iterator --> cannot be subscripted -->we want the values 
    points = result.get_points()
    #Work with dataframes
    list_top_ten_cured = list(points)
    df = DataFrame(list_top_ten_cured)
    #Create dataframe to show table in the terminal
    df.columns = ['Date', 'Confirmed Cases', 'State']
    df = df.astype({'Confirmed Cases':int})
    df = df.set_index('Date')
    df = df.sort_values(by=['Confirmed Cases'])
    df = df.iloc[::-1]
    df = df.iloc[0:10, :]
    print(df)


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
    """
    result_confirmed = DataFrame(list(client.connection.query('SELECT * FROM confirmed_cases').get_points()))
    result_confirmed.columns = ['Date', 'Confirmed Cases', 'State']
    result_confirmed.plot(x='Date', y='Confirmed Cases', kind='line', grid=True, alpha=0.5)


    result_death = DataFrame(list(client.connection.query('SELECT * FROM death_cases').get_points()))
    result_death.columns = ['Date', 'Death Cases', 'State']
    result_death.plot(x='Date', y='Death Cases', kind='line', grid=True, alpha=0.3)

    result_vaccinated = DataFrame(list(client.connection.query('SELECT * FROM vaccinated_person').get_points()))
    result_vaccinated.columns = ['Date', 'State', 'Vaccinated Person']
    result_vaccinated.plot(x='Date', y='Vaccinated Person', kind='line', grid=True, alpha=0.8)
    plt.show()

    fig1 = px.treemap(result_vaccinated, path=['State'], values='Vaccinated Person', title='Cured Cases State Comparison')
    fig1.show()
    fig2 = px.treemap(result_death, path=['State'], values='Death Cases', title='Death Cases State Comparison')
    fig2.show()
    fig3 = px.treemap(result_confirmed, path=['State'], values='Confirmed Cases', title='Vaccinated person State Comparison')
    fig3.show()

    # TODO Show death, confirmed and cured cases within one plot as a line
    # Maybe outsource the treemap



def get_KPIs(client):
    """get KPIs
        get 'key performance indicators', one number gives answer to specific information

        Args:
            client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
        
        Return:
            none

        Test:
            * Are the one number answers printed in the terminal?
    """
    #Get total number of deaths 2021 in the world
    death_2021 = client.connection.query("SELECT CUMULATIVE_SUM(deaths) FROM death_cases WHERE time > '2021-01-01T00:00:00Z'")
    death_2021 = list(death_2021.get_points())
    print(f"The total number of deaths in 2021 is: {int(death_2021[len(death_2021) - 1]['cumulative_sum'])}")

    #Get total number of deaths in Germany 
    germany_deaths = client.connection.query("SELECT CUMULATIVE_SUM(deaths) FROM death_cases WHERE location = 'Germany'")
    germany_deaths = list(germany_deaths.get_points())
    print(f"The total number of deaths in Germany is: {int(germany_deaths[len(germany_deaths) - 1]['cumulative_sum'])}")

    #Get the maximum death cases within a day 
    max_death = client.connection.query("SELECT MAX(deaths), location::tag FROM death_cases")
    max_death = list(max_death.get_points())
    print(f"The maximum number of deaths within a day was {int(max_death[0]['max'])} in {max_death[0]['location']}")