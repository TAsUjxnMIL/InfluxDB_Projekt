import unittest
import pandas as pd
import pandas.testing as pd_testing
from conn_to_DB import MyInfluxDBClient
import get_data_DB



class Test_Influx_Queries(unittest.TestCase):

    client = MyInfluxDBClient()

    # def test_KPIs(self):
    #     actual_array = get_data_DB.get_KPIs(self.client)
    #     expected_array = [1305127, 81492, 4474] 
    #     self.assertEqual(actual_array, expected_array)

    def test_top(self):
        actual_df_top = get_data_DB.get_top_flop(self.client, "TOP")
        expected_df_top = pd.DataFrame({
            'Date':[
                '2021-04-23T00:00:00Z',
                '2021-01-02T00:00:00Z',
                '2021-04-11T00:00:00Z',
                '2021-03-25T00:00:00Z',
                '2021-01-25T00:00:00Z'
            ],
            'Confirmed Cases':[
                346786,
                300310,
                117900,
                100158,
                93822
            ],
            'State':[
                'India',
                'United_States',
                'France',
                'Brazil',
                'Spain'
            ]
        })
        print(expected_df_top)
        # expected_df_top = expected_df_top.astype({'Confirmed Cases': 'int32'}).dtypes
        pd_testing.assert_frame_equal(actual_df_top, expected_df_top)
        

if __name__ == '__main__':
    unittest.main()
        

