"""
This script cleans the 201719Pittsburgh data
"""

import pandas as pd

def main(): 
    all_data = pd.read_csv("201719Pittsburgh.csv")

    # Remove unnecessary columns
    del all_data['Unnamed: 0']
    del all_data['From station id']
    del all_data['To station id']
    del all_data['ï»¿Trip id']

    # convert times to datetime objects
    all_data['Starttime'] = pd.to_datetime(all_data["Starttime"])
    all_data['Stoptime'] = pd.to_datetime(all_data["Stoptime"])

    # create year, month, hour, day of week columns
    all_data['year'] = all_data["Starttime"].dt.year
    all_data['month'] = all_data["Starttime"].dt.month
    all_data['Starthour'] = all_data['Starttime'].dt.hour
    all_data['day_of_week'] = all_data['Starttime'].dt.day_name()

    # convert trip duration to minutes from seconds
    all_data['Tripduration'] = all_data['Tripduration']/60

    # Remove all rows with trip durations over 4 hours long
    # I've determined this number based on the pricing model
    no_outliers_data = all_data[all_data['Tripduration'] < 240]
    
    # Create cleaned csv in current directory
    no_outliers_data.to_csv("201719PittsburghCleaned.csv", index=False)

if __name__ = __'__main__':
    main()
