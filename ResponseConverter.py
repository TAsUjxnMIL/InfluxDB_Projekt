from abc import ABC, abstractmethod

class ResponseConverter(ABC):
    """Response Converter
            * In some functions the data is read from the InfluxDB. The respond cannot be accessed without editing
            * There are some functions that need lists of the data and some need it as dataframe
            * This abstract class holds the function response_Conversion which the child classes implement 

        Args:
            ABC (class): Helper class that provides a standard way to create an ABC using inheritance.
    """
    @abstractmethod
    def responseConversion(self, query_string, client):
        pass