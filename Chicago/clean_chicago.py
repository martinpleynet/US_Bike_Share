"""
This script cleans the 201719Chicago data
"""

import pandas as pd

def main():

    all_data = pd.read_csv("201719Chicago.csv")
    
    # Remove unnecessary columns
    del all_data['from_station_id']
    del all_data['to_station_id']
    del all_data['trip_id']
    del all_data['Unnamed: 0']

    # convert times to datetime objects
    all_data['start_time'] = pd.to_datetime(all_data["start_time"])
    all_data['end_time'] = pd.to_datetime(all_data["end_time"])

    # create year, month, hour, day of week columns
    all_data['year'] = all_data["start_time"].dt.year
    all_data['month'] = all_data["start_time"].dt.month
    all_data['start_hour'] = all_data['start_time'].dt.hour
    all_data['day_of_week'] = all_data['start_time'].dt.day_name()

    # Remove commas from tripdurations
    all_data = all_data.replace(',','', regex=True)

    # convert trip duration to minutes from seconds
    all_data['tripduration']=all_data['tripduration']/60

    # Remove all rows with trip durations over 4 hours long
    # I've determined this number based on the pricing model
    no_outliers_data = all_data[all_data['tripduration'] < 240]

    # create clean csv file in curretn directory
    no_outliers_data.to_csv("201719ChicagoCleaned.csv", index=False)

if __name__=='__main__':
    main()
