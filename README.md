# InfluxDB_Projekt

This database programming project is about the analysis of time series data. The data which is chosen can be found [here](https://ourworldindata.org/coronavirus-source-data) under .csv. This project is written in Python 3.8.5 64-bit ('base': conda). The database which is used is the InfluxDB version: 1.8.4
The main function of the project is to read out data from the database with different queries. Afterwards the result is shown to the user in form of a plot or just a terminal output. 



# Download InfluxDB:
        - Click on this [link] (https://portal.influxdata.com/downloads/). 
        - Go to Are you interested in InfluxDB 1.x? 
        - Select specific InfluxDB version and your platform 

# Set up InfluxDB On Windows: 
        - Copy the link after wget. It could look like this: https://dl.influxdata.com/influxdb/releases/influxdb-1.8.5_windows_amd64.zip
        - Paste this link in to the browser. 
        - Save the appeared Zip file 
        - Unzip this file to your prefered location
        - File should contain:  
                                - influx.exe        (for the CLI utility)
                                - influxd.exe       (to start server)
                                - influxdb.config   (to adapt settings)
                                - influx_inspect.exe
                                - influx_stress.exe
                                - influx_tsm.exe
        - Adapt settings in influxdb.config: location where data, metadata is saved can be changed (optional)
                                - Open the config file
                                - meta: path can be changed in dir = "your\\path\\meta"
                                - data: path can be changed in dir = "your\\path\\data"
                                - wal: path can be changed in wal-dir = "your\\path\\wal"

# Start the server 
    - Navigate in a terminal to the location of the unzipped folder with the .exe and .config files
    - Type in: ./influxd.exe 2> logfile.log (All logs are logged into logfile.log (optional)) 
    - InfluxDB server is started

# Connect to CLI (optional)
    - Open another terminal (location: same as before)
    - Type in: ./influx.exe precision rfc3339 
    - Reason: Interaction with database through terminal
