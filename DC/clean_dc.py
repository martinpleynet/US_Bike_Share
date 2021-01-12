"""
This script cleans the 201719DC data
"""

import pandas as pd

def main():
    
    all_data = pd.read_csv("201719DC.csv")

    # Remove unecessary columns
    del all_data['Start station number']
    del all_data['End station number']
    del all_data['Unnamed: 0']

    # convert times to datetime objects
    all_data['Start date'] = pd.to_datetime(all_data["Start date"])
    all_data['End date'] = pd.to_datetime(all_data["End date"])

    # create year, month, hour, day of week columns
    all_data['year'] = all_data["Start date"].dt.year
    all_data['month'] = all_data["Start date"].dt.month
    all_data['start_hour'] = all_data['Start date'].dt.hour
    all_data['day_of_week'] = all_data['Start date'].dt.day_name()

    # convert trip duration to minutes from seconds
    all_data['Duration'] = all_data['Duration']/60

    # Remove all rows with trip durations over 4 hours long
    # I've determined this number based on the pricing model
    no_outliers_data = all_data[all_data['Duration'] < 240]
    no_outliers_data.head()

    # Create cleaned csv in current directory
    cleaned_data.to_csv("201719DCCleaned.csv", index=False)


if __name__ == '__main__':
    main()
