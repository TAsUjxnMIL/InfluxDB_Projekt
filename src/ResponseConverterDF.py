"""ResponseConverterDF 
   * Child class of abstract class ResponseConverter
  
   Attributes:
        name: Sujan Kanapathipillai
        date: 30.04.2021
        version: 0.0.1 Beta - free
"""
from ResponseConverter import ResponseConverter
from pandas import DataFrame

class ResponseConverterDF(ResponseConverter):
    """Response converter to dataframe
       * Class to avoid always the same code lines. 
       * Holds method which converts InfluxDB response into dataframe

    Args:
        ResponseConverter (ABC): Abstract class which the Response_Converter_df inherits from 
    """
    def responseConversion(self, queryString, client):
        """response conversion
           * Respond of the database is an itereator, which cannot be subscripted
           * To get the actual values this function converts the respond into a dataframe 

        Args:
            self (object reference):
            queryString (string): The query of specific function is saved in here
            client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object

        Returns:
            resultDB_df: Data from database is saved into resultDB_df
        """
        try:
            resultDB = client.connection.query(queryString)  
        except Exception as conError:
            print("Something went wrong: " + str(conError))
            return 
        resultDBlist = list(resultDB.get_points())
        resultDBdf = DataFrame(resultDBlist)
        return resultDBdf
