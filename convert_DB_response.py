from pandas import DataFrame
def response_Conversion(query_string, client):
    """response conversion
        The respond of the database is an itereator, 
        it cannot be subscripted that's why some edits needs to be done

    Args:
        query_string (string): The query of specific function is saved in here
        client (InfluxDBClient object): client contains to connection to the db, queries are executed over this object

    Returns:
        results_DB_df: Data from database is saved into results_DB_df
    """
    results_DB = client.connection.query(query_string)  
    results_DB_list = list(results_DB.get_points())
    results_DB_df = DataFrame(results_DB_list)
    return results_DB_df