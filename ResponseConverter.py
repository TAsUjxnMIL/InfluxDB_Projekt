
"""ResponseConverter
        * This file contains the abstract class ResponseConverter
        * By implementing class multiple function calls could be avoided 
        * In some functions the data is read from the InfluxDB. The respond cannot be accessed without editing
        * There are some functions that need the respond as list and some need it as dataframe
  
   Attributes:
        name: Sujan Kanapathipillai
        date: 30.04.2021
        version: 0.0.1 Beta - free
"""
from abc import ABC, abstractmethod

class ResponseConverter(ABC):
    """ResponseConverter
            * This abstract class holds the function responseConversion which the child classes implement 
        Args:
            ABC (class): Helper class that provides a standard way to create an ABC using inheritance.
    """
    @abstractmethod
    def responseConversion(self, queryString, client):
        pass