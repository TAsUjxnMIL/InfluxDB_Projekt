import matplotlib.pyplot as plt 
import plotly.express as px
from pandas import DataFrame

def get_top_flop_cured(client, choice):
    """Get the ten highest 

    Args:
        client ([type]): [description]
    """
    result = client.query(f'SELECT {choice}("cured", 10), "location"::tag FROM "cured_cases"')
    # Return value is iterator --> cannot be subscripted
    points = result.get_points()
    list_top_ten_cured = list(points)
    df = DataFrame(list_top_ten_cured)
    df.columns = ['Date', 'Confirmed Cases', 'State']
    df = df.astype({'Confirmed Cases':int})
    df = df.set_index('Date')
    df = df.iloc[::-1]
    print(df)


def get_all_data(client):
    """[summary]

    Args:
        client ([type]): [description]
    """
    result_confirmed = DataFrame(list(client.query('SELECT * FROM confirmed_cases').get_points()))
    result_confirmed.columns = ['Date', 'Index', 'Confirmed Cases', 'State']
    result_confirmed.plot(x='Date', y='Confirmed Cases', kind='line', grid=True, alpha=0.5)
    

    result_death = DataFrame(list(client.query('SELECT * FROM death_cases').get_points()))
    result_death.columns = ['Date', 'Index', 'Death Cases', 'State']
    result_death.plot(x='Date', y='Death Cases', kind='line', grid=True, alpha=0.3)

    result_cured = DataFrame(list(client.query('SELECT * FROM cured_cases').get_points()))
    result_cured.columns = ['Date', 'Index', 'Cured Cases', 'State']
    result_cured.plot(x='Date', y='Cured Cases', kind='line', grid=True, alpha=0.8)
    plt.show()

    fig1 = px.treemap(result_cured, path=['State'], values='Cured Cases', title='Cured Cases State Comparison')
    fig1.show()
    fig2 = px.treemap(result_death, path=['State'], values='Death Cases', title='Death Cases State Comparison')
    fig2.show()
    fig3 = px.treemap(result_confirmed, path=['State'], values='Confirmed Cases', title='Confirmed Cases State Comparison')
    fig3.show()

    # TODO Show death, confirmed and cured cases within one plot as a line
    # Maybe outsource the treemap



def get_KPIs(client):
    #Get total number of deaths 2021 in India
    death_2021 = client.connection.query("SELECT SUM(deaths) FROM death_cases WHERE time > '2021-04-23T00:00:00Z'")
    death_2021 = list(death_2021.get_points())
    print(death_2021)

    #
