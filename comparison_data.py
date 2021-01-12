"""
This script contains the data and methods necessary
to create bike share comparison graphs
"""
import matplotlib.pyplot as plt
import numpy as np

# Number of Rides per year
bos_rides =  [1309876, 1762492, 2516146]
chi_rides = [3824761, 3595760, 3809084]
dc_rides = [3748822, 3533594, 3390111]
la_rides = [194786, 304975,285958]
minn_rides = [457206, 408412, 353704]
nyc_rides = [16344391, 17528749, 20528154]
philly_rides = [681690, 666537, 737669]
pitt_rides = [68330, 72218, 107085]
port_rides = [309837, 394561, 321450]

# Number of Bikes per year
bos_bikes = [1799, 4045, 4650]
chi_bikes = [6242, 6133, 6017]
dc_bikes = [4652, 5387, 6053]
la_bikes = [2130, 1443, 5028]
minn_bikes = [0, 2928, 2968] #no bike id in 2017
nyc_bikes = [14201, 15241, 19569]
philly_bikes = [1248, 3114, 1677]
pitt_bikes = [479, 613, 545]
port_bikes = [992, 1020, 1006]


# Number of Stations per year
bos_stat = [287, 336, 357]
chi_stat =[593, 623, 641]
dc_stat = [487, 542, 651]
la_stat = [127, 132, 237]
minn_stat = [202, 205, 181]
nyc_stat = [857, 850, 973]
philly_stat = [126, 141, 148]
pitt_stat = [59, 871, 859]
port_stat = [144, 171, 163]

# City populations per year
#(source: https://www.census.gov/data/tables/time-series/demo/popest/2010s-total-cities-and-towns.html)
bos_pop = [687788, 691147, 692600]
chi_pop = [2711069, 2701423, 2693976]
dc_pop = [694906, 701547, 705749]
la_pop = [3975788, 3977596, 3979576]
minn_pop = [420925, 424903, 429606]
nyc_pop = [8437478, 8390081, 8336817]
philly_pop = [1580601, 1583592, 1584064]
pitt_pop = [301494, 300570, 300286]
port_pop = [647924, 650837, 654741]

#City Land Area in Sq Miles
# Source: Wikipedia
bos_area = 48.42
chi_area = 227.63
dc_area = 61.05
la_area = 468.97
minn_area = 54.00
nyc_area = 302.643
philly_area = 134.28
pitt_area = 55.38
port_area = 133.42

cities = ['Bos', 'Chi', 'DC','LA', 'Minn', 'NYC', 'Philly', 'Pitt', 'Port']

# -----------------------------------------------
# Create Bikes per Thousand People Metric
bos_bpt = [i*1000/j for i, j in zip(bos_bikes, bos_pop)]
chi_bpt = [i*1000/j for i, j in zip(chi_bikes, chi_pop)]
dc_bpt = [i*1000/j for i, j in zip(dc_bikes, dc_pop)]
la_bpt = [i*1000/j for i, j in zip(la_bikes, la_pop)]
minn_bpt = [i*1000/j for i, j in zip(minn_bikes, minn_pop)]
nyc_bpt = [i*1000/j for i, j in zip(nyc_bikes, nyc_pop)]
philly_bpt = [i*1000/j for i, j in zip(philly_bikes, philly_pop)]
pitt_bpt = [i*1000/j for i, j in zip(pitt_bikes, pitt_pop)]
port_bpt = [i*1000/j for i, j in zip(port_bikes, port_pop)]

all_bpt = [bos_bpt,chi_bpt, dc_bpt, la_bpt, minn_bpt, nyc_bpt, philly_bpt, pitt_bpt, port_bpt]

bpt_2017 = []
bpt_2018 = []
bpt_2019 = []
for city in all_bpt:
    bpt_2017.append(city[0])
    bpt_2018.append(city[1])
    bpt_2019.append(city[2])

# create bpt graph
def bpt_graph(filename=None):
    
    plt.style.use('fivethirtyeight')
    fig, ax1 = plt.subplots()
    x = np.arange(len(cities))
    ax1.bar(x-0.2, bpt_2017, width=0.2, label='2017')
    ax1.bar(x, bpt_2018, width=0.2, label='2018')
    ax1.bar(x+0.2, bpt_2019, width=0.2, label='2019')

    ax1.set_xticks(x)
    ax1.set_xticklabels(cities)
    ax1.set_title("Bikes per Thousand People by City")
    ax1.set_ylabel('Num Bikes per Thousand People')
    ax1.set_xlabel('City')
    ax1.legend()

    fig.tight_layout()
    plt.savefig(filename)
    plt.close

# --------------------------------------------------
# Create stations per square mile metric
bos_sps = [x/bos_area for x in bos_stat]
chi_sps = [x/chi_area for x in chi_stat]
dc_sps = [x/dc_area for x in dc_stat]
la_sps = [x/la_area for x in la_stat]
minn_sps = [x/minn_area for x in minn_stat]
nyc_sps = [x/nyc_area for x in nyc_stat]
philly_sps = [x/philly_area for x in philly_stat]
pitt_sps = [x/pitt_area for x in pitt_stat]
port_sps = [x/port_area for x in port_stat]

all_sps = [bos_sps,chi_sps, dc_sps, la_sps, minn_sps, nyc_sps, philly_sps, pitt_sps, port_sps]

sps_2017 = []
sps_2018 = []
sps_2019 = []
for city in all_sps:
    sps_2017.append(city[0])
    sps_2018.append(city[1])
    sps_2019.append(city[2])

# Create sps graph
def sps_graph(filename=None):

    fig, ax2 = plt.subplots()
    x = np.arange(len(cities))
    ax2.bar(x-0.2, sps_2017, width=0.2, label='2017')
    ax2.bar(x, sps_2018, width=0.2, label='2018')
    ax2.bar(x+0.2, sps_2019, width=0.2, label='2019')

    ax2.set_xticks(x)
    ax2.set_xticklabels(cities)
    ax2.set_title("Stations per Square Mile by City")
    ax2.set_ylabel('Num Stations per Square Mile')
    ax2.set_xlabel('City')
    ax2.legend()

    fig.tight_layout()
    plt.savefig(filename)
    plt.close


# ----------------------------------------------------------
# Trips per bicylce per day
bos_tpb = [i/(j*365) for i, j in zip(bos_rides, bos_bikes)]
chi_tpb = [i/(j*365) for i, j in zip(chi_rides, chi_bikes)]
dc_tpb = [i/(j*365) for i, j in zip(dc_rides, dc_bikes)]
la_tpb = [i/(j*365) for i, j in zip(la_rides, la_bikes)]

minn_tpb = []
for i, j in zip(minn_rides, minn_bikes):
    try:
        minn_tpb.append(i/(j*365))
    except ZeroDivisionError:
        minn_tpb.append(0)
        
nyc_tpb = [i/(j*365) for i, j in zip(nyc_rides, nyc_bikes)]
philly_tpb = [i/(j*365) for i, j in zip(philly_rides, philly_bikes)]
pitt_tpb = [i/(j*365) for i, j in zip(pitt_rides, pitt_bikes)]
port_tpb = [i/(j*365) for i, j in zip(port_rides, port_bikes)]

all_tpb = [bos_tpb, chi_tpb, dc_tpb, la_tpb, minn_tpb, nyc_tpb, philly_tpb, pitt_tpb, port_tpb]

tpb_2017 = []
tpb_2018 = []
tpb_2019 = []
for city in all_tpb:
    tpb_2017.append(city[0])
    tpb_2018.append(city[1])
    tpb_2019.append(city[2])

# Create tpb graph
def tpb_graph(filename=None):
    
    fig, ax3 = plt.subplots()
    x = np.arange(len(cities))
    ax3.bar(x-0.2, tpb_2017, width=0.2, label='2017')
    ax3.bar(x, tpb_2018, width=0.2, label='2018')
    ax3.bar(x+0.2, tpb_2019, width=0.2, label='2019')

    ax3.set_xticks(x)
    ax3.set_xticklabels(cities)
    ax3.set_title("Trips per Bike Per Day by City")
    ax3.set_ylabel('Num Trips per Bike Per Day')
    ax3.set_xlabel('City')
    ax3.legend()

    fig.tight_layout()
    plt.savefig(filename)
    plt.close


# ----------------------------------------------------
# Subscriber percentage each year
bos_sub = [84.3, 81.4, 79]
chi_sub = [78.2, 81.3, 77.1]
dc_sub = [74, 78.9, 87.1]
la_sub = [64.1, 53.3, 67.7]
minn_sub = [63.3, 29.7, 50.0] 
nyc_sub = [89.2, 89.0, 86.1]
philly_sub = [85.2, 85.8, 87.9]
pitt_sub = [38.6, 48.2, 51.0]
port_sub = [53.0, 37.8, 36.5]


all_sub = [bos_sub, chi_sub, dc_sub, la_sub, minn_sub, nyc_sub, philly_sub, pitt_sub, port_sub]

sub_2017 = []
sub_2018 = []
sub_2019 = []
for city in all_sub:
    sub_2017.append(city[0])
    sub_2018.append(city[1])
    sub_2019.append(city[2])

# create subscriber graph
def sub_graph(filename=None):
    
    fig, ax4 = plt.subplots()
    x = np.arange(len(cities))
    ax4.bar(x-0.2, sub_2017, width=0.2, label='2017')
    ax4.bar(x, sub_2018, width=0.2, label='2018')
    ax4.bar(x+0.2, sub_2019, width=0.2, label='2019')

    ax4.set_xticks(x)
    ax4.set_xticklabels(cities)
    ax4.set_title("Subscribership Percentage by City")
    ax4.set_ylabel('Subscribership Percentage')
    ax4.set_xlabel('City')
    ax4.legend()

    fig.tight_layout()
    plt.savefig(filename)
    plt.close

# -------------------------------------------------------
# Tripduration median [subscriber, customer] from 2017-2019
bos_td = [10.10, 21.933]
chi_td = [9.617, 24.867]
dc_td = [9.883, 24.250]
la_td = [8.00, 23.00]
minn_td = [8.933, 19.2167]
nyc_td = [9.367, 20.75]
philly_td = [11.00, 21.00]
pitt_td = [10.20, 20.467]
port_td = [9.55, 17.133]

all_td = [bos_td, chi_td, dc_td, la_td, minn_td, nyc_td, philly_td, pitt_td, port_td]

td_sub = []
td_cust = []
for city in all_td:
    td_sub.append(city[0])
    td_cust.append(city[1])

# create trip duration graph
def td_graph(filename=None):
    
    fig, ax5 = plt.subplots()
    x = np.arange(len(cities))
    ax5.bar(x-0.1, td_sub, width=0.2, label='Subscriber')
    ax5.bar(x+0.1, td_cust, width=0.2, label='Customer')

    ax5.set_xticks(x)
    ax5.set_xticklabels(cities)
    ax5.set_title("Trip Duration by City")
    ax5.set_ylabel('Ride Duration (min)')
    ax5.set_xlabel('City')
    ax5.legend()

    fig.tight_layout()
    plt.savefig(filename)
    plt.close

