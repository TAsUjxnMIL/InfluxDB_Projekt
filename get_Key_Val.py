def get_KPIs(client):
    """get KPIs
        get 'key performance indicators', one number gives answer to specific information

        Args:
            client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object
        
        Return:
            result_numbers (array): The KPI values are stored in result_numbers and used for the unittest

        Test:
            * Are the one number answers printed in the terminal?
        
        TODO Determine different categories get_KPIs_Germany, get_KPIs_World,... in different functions
        TODO KPIs separieren drei verschiedene Funnktionen 
    """
    result_numbers = []
    #Get total number of deaths 2021 in the world
    death_2021 = client.connection.query("SELECT CUMULATIVE_SUM(deaths) FROM death_cases WHERE time > '2021-01-01T00:00:00Z'")
    death_2021 = list(death_2021.get_points())
    death_2021 = int(death_2021[len(death_2021) - 1]['cumulative_sum'])
    result_numbers.append(death_2021)
    print(f"\nThe total number of deaths in 2021 is: {death_2021}")

    #Get total number of deaths in Germany 
    germany_deaths = client.connection.query("SELECT CUMULATIVE_SUM(deaths) FROM death_cases WHERE location = 'Germany'")
    germany_deaths = list(germany_deaths.get_points())
    germany_deaths = int(germany_deaths[len(germany_deaths) - 1]['cumulative_sum'])
    result_numbers.append(germany_deaths)
    print(f"The total number of deaths in Germany is: {germany_deaths}")

    #Get the maximum death cases within a day 
    max_death = client.connection.query("SELECT MAX(deaths), location::tag FROM death_cases")
    max_death = list(max_death.get_points())
    print(f"The maximum number of deaths within a day was {int(max_death[0]['max'])} in {max_death[0]['location']}")
    result_numbers.append(int(max_death[0]['max']))

    #Get the mean value of death cases in 2021
    mean_death = client.connection.query("SELECT MEAN(deaths) FROM death_cases WHERE time > '2021-01-01T00:00:00Z'")
    mean_death = list(mean_death.get_points())
    print(f"The mean number of deaths in 2021 is {(mean_death[0]['mean'])}")

    #Get the maximum confirmed cases within a day in 2021 January and the country 
    max_confirmed = client.connection.query("SELECT MAX(confirmed), location::tag FROM confirmed_cases WHERE time >= '2021-01-01T00:00:00Z' AND time <= '2021-02-01T00:00:00Z'")
    max_confirmed = list(max_confirmed.get_points())
    print(f"The maximum number of confirmed cases within a day was {int(max_confirmed[0]['max'])} in {max_confirmed[0]['location']}\n")

    return result_numbers