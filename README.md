# InfluxDB project: Data analysis with corona data

![GitHub repo size](https://img.shields.io/github/repo-size/TAsUjxnMIL/InfluxDB_Projekt)

This database programming project is about the analysis of time series data.
The time series data which is used can be found [here](https://ourworldindata.org/coronavirus-source-data) under .csv.
To run the code in the repository PLEASE use the data within Time_Series_Corona_Data!

The project mainly deals with interacting with the `influx database`. Basic operations like write, read from the database are 
used. After reading, the data is shown to the user either as a terminal output or as a plot. 

This project is written in `Python 3.8.5 64-bit ('base': conda)`. The database which is used is the `InfluxDB version: 1.8.4`

## Table of Contents
1. [Prerequisites](#1.-Prerequisites)
2. [Download InfluxDB on Windows 10](#2.-Download-InfluxDB-Windows-10)
    * [Setting_InfluxDB](#2.1-Settings-InfluxDB)
    * [Start_Server](#2.2-Start-the-server-(Windows-10))
    * [Connect_CLI](#2.3-Connect-to-CLI-Win-optional)
3. [Download InfluxDB on Ubuntu or Mac OS X](#3.-Download-InfluxDB-on-Ubuntu-or-Mac-OS-X)
    * [Start_Server](#3.1-Start-the-server-(Ubuntu-or-Mac))
    * [Connect_CLI](#3.2-Connect-to-CLI-optional)
4. [How to run the project](#4.-How-to-run-the-project-?)


## 1. Prerequisites 

Before cloning this whole project please make sure, you have done the following points:
* Install InfluxDB on your computer
* All the packages needed are installed
  --> Within your python terminal, please enter: `pip install -r requirements.txt`

## 2. Download InfluxDB Windows 10
* Click on this link <https://portal.influxdata.com/downloads/>
* Go to `Are you interested in InfluxDB 1.x?` 
* Select specific InfluxDB version and your platform 
* Copy the link after wget
  (It could look like this: https://dl.influxdata.com/influxdb/releases/influxdb-1.8.5_windows_amd64.zip)
* Paste this link in to the browser. 
* Save the appeared Zip file 
* Unzip this file to your prefered location

### 2.1 Settings InfluxDB
* Unzipped folder should contain:  
    * influx.exe (for the CLI utility)
    * influxd.exe (to start server)
    * influxdb.conf (to adapt settings)
* Adapt settings in influxdb.config: OPTIONAL \
(Location where data, metadata,... is saved, can be changed 
    * Please create meta, data, wal folders within the folder: `influxdb-1.8.5_windows_amd64`
    * Open influxdb.conf
    * meta: path can be changed in `dir =` `"yourpath\\meta"`
    * data: path can be changed in `dir =` `"yourpath\\data"` 
    * wal: path can be changed in `wal-dir =` `"yourpath\\wal"` 

### 2.2 Start the server (Windows 10)
* Navigate in a terminal (Powershell!) to the location of the unzipped folder with the .exe and .conf files
* Type in: `./influxd.exe 2> logfile.log` (if no adaptions were made in influxdb.config)
* Type in: `./influxd.exe -config influxdb.conf 2> logfile.log` (if adaptions were made in influxdb.conf)
* InfluxDB SERVER is started

### 2.3 Connect to CLI Win optional
* Open another terminal (location: same as before)
* Type in: ./influx.exe -precision rfc3339 
* Reason: Interaction with database through terminal
    
    
## 3. Download InfluxDB on Ubuntu or Mac OS X
* Click on this link <https://portal.influxdata.com/downloads/>
* Go to `Are you interested in InfluxDB 1.x?` 
* Select specific InfluxDB version and your platform 
* Enter the instructions given in your terminal

### 3.1 Start the server (Ubuntu or Mac)
* Navigate in a terminal to the location of the unzipped folder with the .exe and .conf files
* In terminal: sudo influxd (Ubuntu)

### 3.2 Connect to CLI optional
* In terminal: sudo influx -precision rfc3339 (Ubuntu)


## 4. How to run the project ?
* Clone the whole InfluxDB_Projekt repository 
* On your machine navigate into the `InfluxDB_Projekt` folder
* Type in `python Program.py` in the terminal \
(Important: program has to be started from within the InfluxDB_Projekt folder)
