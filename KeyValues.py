"""Key values 
   * File contains class KeyPerformanceIndicator 
   * Within class multiple methods which get some key values through specific influxDB queries
   * The return values from methods are used for unittests
   
   Attributes:
        name: Sujan Kanapathipillai
        date: 30.04.2021
        version: 0.0.1 Beta - free      
"""
from DatabaseConnector import MyInfluxDBClient
from ResponseConverterList import ResponseConverterList


class KeyPerformanceIndicator:

    def __init__(self):
        """Init KeyPerformanceIndicator
                * All methods need instance from ResponseConverterList() to convert the data 
                  --> Without, multiple object instanciatings had to be done 
                * All methods need connection to database, so constructor builds object with connection
                * Results from separate methods are saved into resultNumbers
                * self.methods contains all method names of class to invoke them all at once 
        """
        self.converter_list = ResponseConverterList()
        self.client = MyInfluxDBClient()
        self.resultNumbers = []
        self.methods = ["getTotalDeaths", "getDeathGermany", "getMaxDeathDay", "getMeanDeath", "getMaxConfirmed"]

    def getAllKPIs(self):
        """get all KPIs
                * This method invokes all methods defined in self.methods
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        for method in self.methods:
            getattr(self, method)()

    def getTotalDeaths(self):
        """Get total deaths
                * Function gets the total number of deaths in 2021
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        death_2021 = self.converter_list.responseConversion("SELECT CUMULATIVE_SUM(deaths) FROM death_cases \
                     WHERE time > '2021-01-01T00:00:00Z'", self.client)
        death_2021 = int(death_2021[len(death_2021) - 1]['cumulative_sum'])
        self.resultNumbers.append(death_2021)
        print(f"\nThe total number of deaths in 2021 is: {death_2021}")

    def getDeathGermany(self):
        """Get deaths Germany
                * Function gets total amount of deaths in Germany during whole pandamic
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        germany_deaths = self.converter_list.responseConversion("SELECT CUMULATIVE_SUM(deaths) FROM death_cases \
                        WHERE location = 'Germany'", self.client)
        germany_deaths = int(germany_deaths[len(germany_deaths) - 1]['cumulative_sum'])
        self.resultNumbers.append(germany_deaths)
        print(f"The total number of deaths in Germany is: {germany_deaths}")

    def getMaxDeathDay(self):
        """Get max death day
                * Function gets country, number of deaths with the most deaths in a single day 
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        max_death = self.converter_list.responseConversion("SELECT MAX(deaths), location::tag FROM death_cases", self.client)
        print(f"The maximum number of deaths within a day was {int(max_death[0]['max'])} in {max_death[0]['location']}")
        self.resultNumbers.append(int(max_death[0]['max']))

    def getMeanDeath(self):
        """Get mean death 
                * Function gets the mean number of deaths per day in 2021 
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        mean_death = self.converter_list.responseConversion("SELECT MEAN(deaths) FROM death_cases \
                     WHERE time > '2021-01-01T00:00:00Z'", self.client)
        print(f"The mean number of deaths in 2021 is {(mean_death[0]['mean'])}")

    def getMaxConfirmed(self):
        """Get max confirmed 
                * Function gets the maximum number of confirmed cases in the world and its country 
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        max_confirmed = self.converter_list.responseConversion("SELECT MAX(confirmed), location::tag FROM confirmed_cases \
                        WHERE time >= '2021-01-01T00:00:00Z' AND time <= '2021-02-01T00:00:00Z'", self.client)
        print(f"The maximum number of confirmed cases within a day was {int(max_confirmed[0]['max'])} in {max_confirmed[0]['location']}\n")