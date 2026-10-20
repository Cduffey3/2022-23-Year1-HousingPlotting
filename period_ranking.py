"""
Connor Duffey
CS 141
Period ranking file
"""

import index_tools as it

def sort_tuple(tup):
    """
    given a list of tuples will sort them using the value
    param:
        Unsorted list
    returns a sorted list
    """
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


def quarter_data(data, year, qtr):
    """
    Gets the data at a given year and qtr and sorts it highest to lowest
        data -> dictonary
        year -> int or string converter to int later
    """
    unsorted = []
    for key in data:
        for item in data[key]:
            if item.year == int(year) and item.qtr == int(qtr):
                unsorted.append((key, item.index))
            else:
                continue
    sortlist = sort_tuple(unsorted)
    i = len(sortlist)-1
    rever = []
    while i >= 0:
        rever.append(sortlist[i])
        i -= 1
    return rever

def annual_data(data, year):
    """
    Gets the data at a given year and sorts it highest to lowest
    param:
        data -> dictonary
        year -> int or string converter to int later
    return sorted list
    """
    unsorted = []
    for key in data:
        for item in data[key]:
            if item.year == int(year):
                unsorted.append((key, item.index))
            else:
                continue
    sortlist = sort_tuple(unsorted)
    i = len(sortlist)-1
    rever = []
    while i >= 0:
        rever.append(sortlist[i])
        i -= 1
    return rever

def main():
    """
    docstring for the main function here
    """
    x = input("Enter region-based house price index filename:")
    command = "data/" + x
    y = input("Enter year of interest for house prices:")
    z = input("Enter qtr of interest:")
    data = it.read_state_house_price_data(command)
    data1 = it.annualize(data)
    list = quarter_data(data, y, z)
    it.print_ranking(list)



if __name__ == '__main__':
    # main runs only when directly invoking this module
    main()

