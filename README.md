# InfluxDB project: Data analysis with corona data

![GitHub repo size](https://img.shields.io/github/repo-size/TAsUjxnMIL/InfluxDB_Projekt)

This database programming project is about the analysis of time series data.
The time series data which is used can be found [here](https://ourworldindata.org/coronavirus-source-data) under .csv.
To run the code in the repository PLEASE use the data within Time_Series_Corona_Data!

The project mainly deals with interacting with the `influx database`. Basic operations like write, read from the database are 
used. After reading the data is shown to the user either as a terminal output or as a plot. 

This project is written in `Python 3.8.5 64-bit ('base': conda)`. The database which is used is the `InfluxDB version: 1.8.4`

## Table of Contents
1. [Prerequisites](#Prerequisites)
2. [Download InfluxDB on Windows 10](#Download-InfluxDB-Windows-10)
    * [Setting_InfluxDB](#Settings-InfluxDB)
    * [Start_Server](#Start-the-server)
    * [Connect_CLI_Win](#Connect-to-CLI-Win-optional)
3. [Download InfluxDB on Ubuntu/ Mac OS X](#Download-InfluxDB-on-Ubuntu/-Mac-OS-X)
    * [Start_Server](#Start-the-server)
    * [Connect_CLI](#Connect-to-CLI-optional)





## Prerequisites 

Before cloning this whole project please make sure, you have done the following points:
* Install InfluxDB on your computer
* All the packages needed are installed
  --> Within your python terminal, please enter: `pip install -r packages.txt`

## Download InfluxDB Windows 10
* Click on this link <https://portal.influxdata.com/downloads/>
* Go to `Are you interested in InfluxDB 1.x?` 
* Select specific InfluxDB version and your platform 
* Copy the link after wget
  (It could look like this: https://dl.influxdata.com/influxdb/releases/influxdb-1.8.5_windows_amd64.zip)
* Paste this link in to the browser. 
* Save the appeared Zip file 
* Unzip this file to your prefered location

### Settings InfluxDB
* Unzipped folder should contain:  
    * influx.exe        (for the CLI utility)
    * influxd.exe       (to start server)
    * influxdb.conf     (to adapt settings)
    * influx_inspect.exe
    * influx_stress.exe
    * influx_tsm.exe
* Adapt settings in influxdb.config: location where data, metadata is saved can be changed (optional)
    * Please create meta, data, wal folders within `influxdb-1.8.5_windows_amd64`
    * Open influxdb.conf
    * meta: path can be changed in dir = `"yourpath\\meta"` 
    * data: path can be changed in dir = `"yourpath\\data"` 
    * wal: path can be changed in wal-dir = `"yourpath\\wal"` 

### Start the server (Win)
* Navigate in a terminal to the location of the unzipped folder with the .exe and .conf files
* Type in: `./influxd.exe 2> logfile.log` (if no adaptions were made in influxdb.config)
* Type in: `./influxd.exe -config influxdb.conf 2> logfile.log` (if adaptions were made in influxdb.conf)
* InfluxDB SERVER is started

### Connect to CLI Win optional
* Open another terminal (location: same as before)
* Type in: ./influx.exe -precision rfc3339 
* Reason: Interaction with database through terminal
    
    
## Download InfluxDB on Ubuntu/ Mac OS X
* Click on this link <https://portal.influxdata.com/downloads/>
* Go to `Are you interested in InfluxDB 1.x?` 
* Select specific InfluxDB version and your platform 
* Enter the instructions given in your terminal

### Start the server
* Navigate in a terminal to the location of the unzipped folder with the .exe and .conf files
* In terminal: sudo influxd (Ubuntu)

### Connect to CLI optional
* In terminal: sudo influx -precision rfc3339 (Ubuntu)
