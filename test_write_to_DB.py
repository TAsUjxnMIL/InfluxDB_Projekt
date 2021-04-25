import pandas as pd 

class Corona_Data:
    
    def __init__(self, _file_path, _date, _state, _vaccinated, _confirmed, _deaths, _client):
        self.file_path = _file_path
        self.client = _client
        # self.date = _date
        # self.state = _state
        # self.vaccinated = _vaccinated
        # self.confirmed = _confirmed
        # self.deaths = _deaths

    def read_Data_From_CSV(self):
        self.csvReader = pd.read_csv(self.file_path)
        # Set variables 
        self.date = self.csvReader.date
        #tags = csvReader.iso_code
        self.state = self.csvReader.location.str.replace(" ", "_", case=False) #tag should not contain blank spaces
        self.vaccinated = self.csvReader.new_vaccinations
        self.confirmed = self.csvReader.new_cases
        self.deaths = self.csvReader.new_deaths

    def write_To_DB(self):
        #Setup Payload 
        json_payload = []
        for i in range(1, len(self.csvReader)):
            confirmed_json = {
                "measurement": "confirmed_cases",
                "tags":{
                    "location": self.state[i]
                },
                "time": self.date[i],
                "fields":{
                    'confirmed': self.confirmed[i]
                }
            }
    
            death_json = {
                "measurement": "death_cases",
                "tags":{
                    "location": self.state[i]
                },
                "time": self.date[i],
                "fields":{
                    'deaths': self.deaths[i]
                }
            }

            vaccinated_json = {
                "measurement": "vaccinated_person",
                "tags":{
                    "location": self.state[i]
                },
                "time": self.date[i],
                "fields":{
                    'vaccinated': self.vaccinated[i]
                }
            }


            json_payload.append(confirmed_json)
            json_payload.append(death_json)
            json_payload.append(vaccinated_json)
            # client = con.setContoInflux()
        _ = self.client.write_points(json_payload)

