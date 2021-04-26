import unittest
import pandas as pd
import pandas.testing as pd_testing
from conn_to_DB import MyInfluxDBClient
import get_data_DB



class Test_Influx_Queries(unittest.TestCase):

    client = MyInfluxDBClient()

    def test_KPIs(self):
        actual_array = get_data_DB.get_KPIs(self.client)
        expected_array = [1305127, 81492, 4474] 
        self.assertEqual(actual_array, expected_array)

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
        expected_df_top['Confirmed Cases'] = expected_df_top['Confirmed Cases'].astype("int32")
        pd_testing.assert_frame_equal(actual_df_top, expected_df_top)
        
    def test_flop(self):
        actual_df_flop = get_data_DB.get_top_flop(self.client, "BOTTOM")
        expected_df_flop = pd.DataFrame({
            'Date':[
                '2020-02-19T00:00:00Z',
                '2020-01-29T00:00:00Z',
                '2020-03-05T00:00:00Z',
                '2020-03-21T00:00:00Z',
                '2020-03-26T00:00:00Z'
            ],
            'Confirmed Cases':[
                2,
                0,
                0,
                0,
                0
            ],
            'State':[
                'Iran',
                'Germany',
                'Hungary',
                'Haiti',
                'Guinea-Bissau'
            ]
        })
        expected_df_flop['Confirmed Cases'] = expected_df_flop['Confirmed Cases'].astype("int32")
        pd_testing.assert_frame_equal(actual_df_flop, expected_df_flop)



if __name__ == '__main__':
    unittest.main()
        

