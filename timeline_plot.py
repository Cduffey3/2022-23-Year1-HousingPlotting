"""
Connor Duffey
CS 141
Prof Steele
timeline plotting file
"""
import numpy as np
# import numpy’s ma submodule using the alias ma
import index_tools as it
import numpy.ma as ma
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import copy

def build_plottable_array(xyears, regiondata):
    """
    takes in a list of ints and a dict based on a region and returns a masked array
    param:
        xyears -> list of years
        regiondata -> list of values
    """
    lst = []
    i = 0
    while i < len(xyears):
        for value in regiondata:
            if value.year == xyears[i]:
                val = value.index
                break
            else:
                val = "--"
                continue
        lst.append(val)
        i += 1
    mask = []
    for item in lst:
        if item == "--":
            mask.append(1)
        else:
            mask.append(0)
    yValues = ma.masked_array(lst, mask)
    return yValues

def filter_years(data, year0, year1):
    """
    Iterates through a dictionary and only holds onto the values between the years returns a dictionary
    param:
        data -> dictonary
        year0 -> int or string is converted to an int for comparison
        year1 -> same as year0
    """
    diction = dict()
    for key in data:
        for item in data[key]:
            if item.year >= int(year0) and item.year <= int(year1):
                it.add_values_in_dict(diction, key, item)
            else:
                continue
    return diction

def plot_HPI(data, regionlist):
    """
    Demonstrates a line graph  no return value
    """
    for region in regionlist:
        for key in data:
            values = []
            when = []
            if key == region:
                for item in data[key]:
                    values.append(float(item.index))
                    when.append(int(item.year))
            else:
                continue

            plt.plot(when, values, marker= "x", label = key)
            plt.title("Home Prices Indices: " + str(when[0]) +"-"+ str(when[(len(when)-1)]))
            plt.legend()
    plt.show()

def plot_whiskers(data, regionlist):
    """
    doesnt work dont bother
    """
    for region in regionlist:
        for keys in data:
            values = []
            if keys == region:
                for item in data[keys]:
                    values.append(item.index)
            plt.plot(values)
    plt.show()


def main():
    """
    docstring for the main function here
    """
    x = input("Enter house price index filename:")
    start = int(input("Enter the start year of the range to plot:"))
    end = int(input("Enter the end year of the range to plot: "))
    command = "data/" + x
    if x[-5] != "5":
        data = it.read_state_house_price_data(command)
        regionlst = []
        region = input("Enter next region for plots (<ENTER> to stop):")
        while region != "":
            regionlst.append(region)
            region = input("Enter next region for plots (<ENTER> to stop):")
        i = 0
        while i < len(regionlst):
            it.print_range(data, regionlst[i])
            i += 1
        plot_HPI(it.annualize(filter_years(data, start, end)), regionlst)
        plot_whiskers(it.annualize(filter_years(data, start, end)), regionlst)
    else:
        regionlst = []
        region = input("Enter next region for plots (<ENTER> to stop):")
        while region != "":
            regionlst.append(region)
            region = input("Enter next region for plots (<ENTER> to stop):")
        data = it.read_zip_house_price_data(command)
        i = 0
        while i < len(regionlst)-1:
            it.print_range(data, regionlst[i])
            i += 1
        plot_HPI(it.annualize(filter_years(data, start, end)), regionlst)
        plot_whiskers(it.annualize(filter_years(data, start, end)), regionlst)

if __name__ == '__main__':
    # main runs only when directly invoking this module
    main()