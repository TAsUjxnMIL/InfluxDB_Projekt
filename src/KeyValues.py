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

    def getAllKPIs(self, terminalOutput=True):
        """get all KPIs
                * This method invokes all methods defined in self.methods
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        for method in self.methods:
            getattr(self, method)(terminalOutput)

    def getTotalDeaths(self, terminalOutput):
        """Get total deaths
                * Function gets the total number of deaths in 2021
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        death2021 = self.converter_list.responseConversion("SELECT CUMULATIVE_SUM(deaths) FROM death_cases \
                     WHERE time > '2021-01-01T00:00:00Z'", self.client)
        death2021 = int(death2021[len(death2021) - 1]['cumulative_sum'])
        self.resultNumbers.append(death2021)
        if terminalOutput:
            print(f"\nThe total number of deaths in 2021 is: {death2021}")

    def getDeathGermany(self, terminalOutput):
        """Get deaths Germany
                * Function gets total amount of deaths in Germany during whole pandamic
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        germanyDeaths = self.converter_list.responseConversion("SELECT CUMULATIVE_SUM(deaths) FROM death_cases \
                        WHERE location = 'Germany'", self.client)
        germanyDeaths = int(germanyDeaths[len(germanyDeaths) - 1]['cumulative_sum'])
        self.resultNumbers.append(germanyDeaths)
        if terminalOutput:
            print(f"The total number of deaths in Germany is: {germanyDeaths}")

    def getMaxDeathDay(self, terminalOutput):
        """Get max death day
                * Function gets country, number of deaths with the most deaths in a single day 
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        maxDeath = self.converter_list.responseConversion("SELECT MAX(deaths), location::tag FROM death_cases", self.client)
        self.resultNumbers.append(int(maxDeath[0]['max']))
        if terminalOutput:
            print(f"The maximum number of deaths within a day was {int(maxDeath[0]['max'])} in {maxDeath[0]['location']}")

    def getMeanDeath(self, terminalOutput):
        """Get mean death 
                * Function gets the mean number of deaths per day in 2021 
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        meanDeath = self.converter_list.responseConversion("SELECT MEAN(deaths) FROM death_cases \
                     WHERE time > '2021-01-01T00:00:00Z'", self.client)
        self.resultNumbers.append(round(meanDeath[0]['mean'],3))
        if terminalOutput:
            print(f"The mean number of deaths in 2021 is {(meanDeath[0]['mean'])}")

    def getMaxConfirmed(self, terminalOutput):
        """Get max confirmed 
                * Function gets the maximum number of confirmed cases in the world and its country 
            Args:
                self (instanced object): By using self attributes and methods of class can be accessed
        """
        maxConfirmed = self.converter_list.responseConversion("SELECT MAX(confirmed), location::tag FROM confirmed_cases \
                        WHERE time >= '2021-01-01T00:00:00Z' AND time <= '2021-02-01T00:00:00Z'", self.client)
        self.resultNumbers.append(int(maxConfirmed[0]['max']))
        if terminalOutput:
            print(f"The maximum number of confirmed cases within a day was {int(maxConfirmed[0]['max'])} in {maxConfirmed[0]['location']}\n")
                    