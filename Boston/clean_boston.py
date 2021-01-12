"""
This script cleans the 201719Boston data
"""

import pandas as pd

def main(): 
    all_data = pd.read_csv("201719Boston.csv")

    # Remove unnecessary columns
    del all_data['start station id']
    del all_data['end station id']
    del all_data['start station latitude']
    del all_data['start station longitude']
    del all_data['end station latitude']
    del all_data['end station longitude']
    del all_data['Unnamed: 0']

    # convert times to datetime objects
    all_data['starttime'] = pd.to_datetime(all_data["starttime"])
    all_data['stoptime'] = pd.to_datetime(all_data["stoptime"])

    # create year, month, hour, day of week columns
    all_data['year'] = all_data["starttime"].dt.year
    all_data['month'] = all_data["starttime"].dt.month
    all_data['start_hour'] = all_data['starttime'].dt.hour
    all_data['day_of_week'] = all_data['starttime'].dt.day_name()

    # convert trip duration to minutes from seconds
    all_data['tripduration'] = all_data['tripduration']/60

    # Remove all rows with trip durations over 4 hours long
    # I've determined this number based on the pricing model
    no_outliers_data = all_data[all_data['tripduration'] < 240]

    # Create cleaned csv in current directory
    no_outliers_data.to_csv("201719BostonCleaned.csv", index=False)

if __name__ == '__main__':
    main()



    

