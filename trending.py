"""
Connor Duffey
CS 141
Prof Steele
trending file
"""

import index_tools as it
import period_ranking

def cagr(idxlist, periods):
    """
    given a value you will calcuate the aver change the year
    param:
        idxlist -> 2 string values in format (lower, higher)
        periods -> int
    return:
        float
    """
    CAGR = 0
    inner = float(idxlist[1])/float(idxlist[0])
    afterexpon = float(inner ** (1/int(periods)))
    beforeper = float(afterexpon - 1)
    CAGR = float(beforeper * 100)
    return CAGR

def calculate_trends(data, year0, year1):
    """
    using the cagr function to calcualt treds of all the data for compersion
    param:
        data -> dict
        year0 -> string or int converted to int anyway
        year1 -> same as year 0
    return:
        sorted listed
    """
    unsorted = []
    idxlist = []
    for key in data:
        for item in data[key]:
            if item.year == int(year0):
                fyear = True
                val1 = float(item.index)
            elif item.year == int(year1):
                syear = True
                val2 = float(item.index)
        if fyear == True and syear == True:
            idxlist = [val1, val2]
            trend = cagr(idxlist, (int(year1)-int(year0)))
            unsorted.append((key, trend))
        else:
            continue
    ltoh = period_ranking.sort_tuple(unsorted)
    sorted = []
    i = len(ltoh) - 1
    while i >= 0:
        sorted.append(ltoh[i])
        i -= 1
    return sorted

def main():
    """
    docstring for the main function here
    """
    x = input("Enter file name")
    command = "data/" + x
    year1 = int(input("Enter start year of intrest: "))
    year2 = int(input("Enter end year of intrest: "))
    data = it.read_state_house_price_data(command)
    print(year1, "-", year2, "Compound Annual Growth Rate")
    ranks = calculate_trends(data, year1, year2)
    it.print_ranking(ranks)

if __name__ == '__main__':
    # main runs only when directly invoking this module
    main()