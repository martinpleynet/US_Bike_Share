"""
This script cleans the 201719Portland data
"""
import pandas as pd

def main(): 
    all_data = pd.read_csv("201719Portland.csv")

    # Remove unnecessary columns
    del all_data['RouteID']
    del all_data['StartLatitude']
    del all_data['StartLongitude']
    del all_data['EndLatitude']
    del all_data['EndLongitude']
    del all_data['RentalAccessPath']
    del all_data['MultipleRental']
    del all_data['Start_Latitude']
    del all_data['Start_Longitude']
    del all_data['End_Latitude']
    del all_data['End_Longitude']
    del all_data['Distance_Miles_']
    del all_data['TripType']

    # Concatenate StartDate and StartTime columns
    # Concatenate EndDate and EndTime columns
    all_data['StartDate'] = all_data['StartDate'] + ' ' + all_data['StartTime']
    all_data['EndDate'] = all_data['EndDate'] + ' ' + all_data['EndTime']

    # Remove cloumns after concat
    del all_data['StartTime']
    del all_data['EndTime']

    # convert times to datetime objects
    all_data['StartDate'] = pd.to_datetime(all_data["StartDate"])
    all_data['EndDate'] = pd.to_datetime(all_data["EndDate"])

    # create year, month, hour, day of week columns
    all_data['year'] = all_data["StartDate"].dt.year
    all_data['month'] = all_data["StartDate"].dt.month
    all_data['Starthour'] = all_data['StartDate'].dt.hour
    all_data['dayofweek'] = all_data['StartDate'].dt.day_name()

    # clean Duration column into appropriate workable format
    dur_split = all_data['Duration'].str.split(':', n = 2, expand=True)
    
    dur_split[0]=dur_split[0].astype(float)
    dur_split[1]=dur_split[1].astype(float)
    dur_split[2]=dur_split[2].astype(float)
    
    all_data['DurationMin'] = 60*dur_split[0] + dur_split[1] + dur_split[2]/60

    del all_data['Duration']

    # Remove all rows with trip durations over 4 hours long
    # I've determined this number based on the pricing model
    no_outliers_data = all_data[all_data['DurationMin'] < 240]

    # Create cleaned csv in current directory
    no_outliers_data.to_csv("201719PortlandCleaned.csv", index=False)

if __name__ == '__main__':
    main()




