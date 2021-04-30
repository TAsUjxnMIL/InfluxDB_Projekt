"""Program start point 
   * Main function where the data analysis is started
   * User is able to choose between multiple functions which can be executed
   
   Attributes:
        name: Sujan Kanapathipillai
        date: 30.04.2021
        version: 0.0.1 Beta - free
         
"""
from DatabaseConnector import MyInfluxDBClient
from ResponseConverterList import ResponseConverterList


class KeyPerformanceIndicator:

    def __init__(self):
        self.converter_list = ResponseConverterList()
        self.client = MyInfluxDBClient()
        self.result_numbers = []
        self.methods = ["getTotalDeaths", "getDeathGermany", "getMaxDeathDay", "getMeanDeath", "getMaxConfirmed"]

    def getAllKPIs(self):
        """get all KPI values
            This method invokes all methods defined in self.methods

            source: https://stackoverflow.com/questions/37075680/run-all-functions-in-class
        """
        for method in self.methods:
            getattr(self, method)()

    def getTotalDeaths(self):
        death_2021 = self.converter_list.responseConversion("SELECT CUMULATIVE_SUM(deaths) FROM death_cases \
                     WHERE time > '2021-01-01T00:00:00Z'", self.client)
        death_2021 = int(death_2021[len(death_2021) - 1]['cumulative_sum'])
        self.result_numbers.append(death_2021)
        print(f"\nThe total number of deaths in 2021 is: {death_2021}")

    def getDeathGermany(self):
        germany_deaths = self.converter_list.responseConversion("SELECT CUMULATIVE_SUM(deaths) FROM death_cases \
                        WHERE location = 'Germany'", self.client)
        germany_deaths = int(germany_deaths[len(germany_deaths) - 1]['cumulative_sum'])
        self.result_numbers.append(germany_deaths)
        print(f"The total number of deaths in Germany is: {germany_deaths}")

    def getMaxDeathDay(self):
        #Get the maximum death cases within a day 
        max_death = self.converter_list.responseConversion("SELECT MAX(deaths), location::tag FROM death_cases", self.client)
        print(f"The maximum number of deaths within a day was {int(max_death[0]['max'])} in {max_death[0]['location']}")
        self.result_numbers.append(int(max_death[0]['max']))

    def getMeanDeath(self):
        #Get the mean value of death cases in 2021
        mean_death = self.converter_list.responseConversion("SELECT MEAN(deaths) FROM death_cases \
                     WHERE time > '2021-01-01T00:00:00Z'", self.client)
        print(f"The mean number of deaths in 2021 is {(mean_death[0]['mean'])}")

    def getMaxConfirmed(self):
        #Get the maximum confirmed cases within a day in 2021 January and the country 
        max_confirmed = self.converter_list.responseConversion("SELECT MAX(confirmed), location::tag FROM confirmed_cases \
                        WHERE time >= '2021-01-01T00:00:00Z' AND time <= '2021-02-01T00:00:00Z'", self.client)
        print(f"The maximum number of confirmed cases within a day was {int(max_confirmed[0]['max'])} in {max_confirmed[0]['location']}\n")