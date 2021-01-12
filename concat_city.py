"""
This script combines all the files within a directory
over a 3-year period into one csv file
"""

import pandas as pd
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path',
                        help='realtive path to directory of monthly/quarterly files')
    parser.add_argument('city_name', help='name of city')
    args = parser.parse_args()


    files = [file for file in os.listdir(args.dir_path)]
    all_years_data = pd.DataFrame()

    for file in files:
        df = pd.read_csv(args.dir_path + file)
        all_years_data = pd.concat([all_years_data, df])

    all_years_data.to_csv(f"201719{args.city_name}.csv", index=False)


if __name__=='__main__':
    main()

