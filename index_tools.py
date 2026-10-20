"""
Connor Duffey
CS 141
Index tools document for the homeprices project
"""
from dataclasses import dataclass

@dataclass
class QuarterHPI:
    year: int
    qtr: int
    index: float

@dataclass
class AnnualHPI:
    year: int
    index: float

def add_values_in_dict(sample_dict, key, value):
    ''' Append multiple values to a key in
        the given dictionary '''
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].append(value)
    return sample_dict

def read_state_house_price_data(string):
    """
    Function takes a string that is a file path to a text file and will return a list of Quarter HPI
    fails with in proper params and prints saying data unavalible
    """
    diction = dict()
    file = open(string)
    for line in file:
        x = line.split(" ")
        y = line.split("\t")
        key = y[0]
        year = y[1]
        qtr = y[2]
        index = y[3]
        if year[0] != "1" and year[0] != "2":
            continue
        elif index[0] == ".":
            print(line)
        else:
            diction = add_values_in_dict(diction, key, (QuarterHPI(int(year), int(qtr), float(index))))
    return diction

def read_zip_house_price_data(string):
    """
    Opens the zip code file and then takes those values and puts them into the anHPI class and ties those with the zip code to return a dictonary
    """
    counted = 0
    uncounted = 0
    dict1 = dict()
    file = open(string)
    for line in file:
        x = line.split(" ")
        y = line.split("\t")
        key = y[0]
        year = y[1]
        index = y[3]
        if year[0] != "1" and year[0] != "2":
            continue
        elif index == ".":
            uncounted += 1
        else:
            counted += 1
            dict1 = add_values_in_dict(dict1, key, (AnnualHPI(int(year), float(index))))
    print("Counted: " + str(counted) + " Uncounted: " + str(uncounted))
    return dict1

def index_range(data, state):
    """
    finds the highes and lowest vaule of a given state
    """
    slist = data[state]
    highest = slist[0]
    lowest = slist[0]
    i = 1
    while i < len(slist):
        temp = float(slist[i].index)
        if temp > highest.index:
            highest = slist[i]
            i += 1
        elif temp < lowest.index:
            lowest = slist[i]
            i += 1
        else:
            i += 1
    return (lowest, highest)

def print_range(data, state):
    """
    Using the value that was given in index range, and then fance prints it
    """
    sttuple = index_range(data, state)
    print("Region:", state)
    if sttuple[0] == QuarterHPI:
        print("Low: year/quarter/index:", sttuple[0].year, "/", sttuple[0].qtr , "/", sttuple[0].index)
        print("High: year/quarter/index:", sttuple[1].year, "/", sttuple[1].qtr, "/", sttuple[1].index)
    else:
        print("Low: year/quarter/index:", sttuple[0].year, "/", sttuple[0].index)
        print("High: year/quarter/index:", sttuple[1].year, "/", sttuple[1].index)
    return None

def print_ranking(data, heading="Ranking"):
    """
    prints the top ten highest index values
    prints the lowest ten index values and only works for states not zips
    """
    lowlist = []
    highlist = []
    i = 0
    while i < 10:
        highlist.append(data[i])
        i += 1
    j = len(data)-1
    while j > (len(data) - 11):
        lowlist.append(data[j])
        j -= 1
    print("The Top 10")
    count1 = 0
    count2 = 41
    for item in highlist:
        count1 += 1
        print(count1, ":", item )
    print("The Bottom 10")
    x = len(lowlist)-1
    while x >= len(lowlist)-10:
        count2 += 1
        print(count2 , ":", lowlist[x])
        x -= 1
    return None

def annualize(data):
    """
    iterates through quarterHPI's to turn them into annuals
    returns a dict of these new values
    """
    dict1 = dict()
    for key in data:
        templist = data[key]
        i = 0
        qtr = 0
        total = 0
        while i < (len(templist)-1):
            if templist[i+1].year == templist[i].year and templist[i+1] != None:
                if templist[i] != ".":
                    qtr += 1
                    total += float(templist[i].index)
                    i += 1
                else:
                    i += 1
            elif templist[i].year == templist[i-1].year:
                if templist[i] != ".":
                    qtr += 1
                    total += float(templist[i].index)
                    dict1 = add_values_in_dict(dict1, key, (AnnualHPI(int(templist[i].year), float(total/qtr))))
                    i += 1
                    qtr = 0
                    total = 0
                else:
                    dict1 = add_values_in_dict(dict1, key, (AnnualHPI(int(templist[i].year), float(total/qtr))))
                    i += 1
                    qtr = 0
                    total = 0
    return dict1

def main():
    """
    docstring for the main function here
    """
    x = input("Enter file name")
    command = "data/" + x
    data = read_state_house_price_data(command)
    region = input("enter region of interest:")
    while region != "":
        print_range(data, region)
        data2 = annualize(data)
        print_range(data2, region)
        for key in data2:
            if key == region:
                print(data2[key])
        region = input("enter region of interest:")

if __name__ == '__main__':
    # main runs only when directly invoking this module
    main()

# end of program file
