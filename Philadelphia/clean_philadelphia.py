"""
This script cleans the 201719Philadelphia data
"""

import pandas as pd

def main(): 
    all_data = pd.read_csv("201719Philadelphia.csv")

    # Remove unnecessary columns
    del all_data['trip_id']
    del all_data['start_lat']
    del all_data['start_lon']
    del all_data['end_lat']
    del all_data['end_lon']
    del all_data['plan_duration']
    del all_data['trip_route_category']

    # convert times to datetime objects
    all_data['start_time'] = pd.to_datetime(all_data["start_time"])
    all_data['end_time'] = pd.to_datetime(all_data["end_time"])

    # create year, month, hour, day of week columns
    all_data['year'] = all_data["start_time"].dt.year
    all_data['month'] = all_data["start_time"].dt.month
    all_data['start_hour'] = all_data['start_time'].dt.hour
    all_data['day_of_week'] = all_data['start_time'].dt.day_name()

    # Remove all rows with trip durations over 4 hours long
    # I've determined this number based on the pricing model
    no_outliers_data = all_data[all_data['duration'] < 240]

    # Reassign passholder_type to Subscriber and Customer accordingly
    no_outliers_data.replace({'Indego30':'Subscriber', 'Indego365':'Subscriber', 'Day Pass':'Customer', 'Walk-up':'Customer', 'IndegoFlex':'Customer', 'One Day Pass':'Customer', 'Two Day Pass':'Customer'}, inplace=True)

    # Create cleaned csv in current directory
    no_outliers_data.to_csv("201719PhiladelphiaCleaned.csv", index=False)

if __name__ = '__main__':
    main()
