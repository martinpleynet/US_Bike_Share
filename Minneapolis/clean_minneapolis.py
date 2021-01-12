"""
This script cleans the 201719Minneapolis data
"""

import pandas as pd

def main(): 
    all_data = pd.read_csv("201719Boston.csv")

    # Remove unnecessary columns
    del all_data['start station id']
    del all_data['start station latitude']
    del all_data['start station longitude']
    del all_data['end station id']
    del all_data['end station latitude']
    del all_data['end station longitude']
    del all_data['Unnamed: 0']

    # convert times to datetime objects
    all_data['start_time'] = pd.to_datetime(all_data["start_time"])
    all_data['end_time'] = pd.to_datetime(all_data["end_time"])

    # create year, month, hour, day of week columns
    all_data['year'] = all_data["start_time"].dt.year
    all_data['month'] = all_data["start_time"].dt.month
    all_data['start_hour'] = all_data['start_time'].dt.hour
    all_data['day_of_week'] = all_data['start_time'].dt.day_name()

    # no data for columns 5, 7, 8, 9 for 2017
    # as the data was not collected until 2018

    # convert trip duration to minutes from seconds
    all_data['tripduration'] = all_data['tripduration']/60

    # Remove all rows with trip durations over 4 hours long
    # I've determined this number based on the pricing model
    no_outliers_data = all_data[all_data['tripduration'] < 240]

    # reassign usertypes to Subscriber and Customer
    no_outliers_data['usertype'] = no_outliers_data['usertype'].replace({"Member": "Subscriber","Casual": "Customer"})

    # Create cleaned csv in current directory
    no_outliers_data.to_csv("201719MinneapolisCleaned.csv", index=False)

if __name__ == '__main__':
    main()

    
