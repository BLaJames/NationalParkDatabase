# James La, jbla@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Final Project
# interface.py
# Description: Reads CSV file with information on national parks; sorts through file to get information that is
# displayed depending on user's choice
# Describe what this file does: Calls functions from tasks to create functions that sort out information from CSV file
# for user

import tasks  # import tasks to incorporate into interface


def getMenuDict():  # define function to obtain menu
    # create dictionary for menu
    menuDict = {"A": "All national parks", "B": "Parks in a particular state", "C": "The largest park",
                "D": "Search for a park", "E": "The oldest park", "F": "State with most parks", "Q": "Quit"}

    return menuDict  # return dictionary


def displayMenu(menuDict):  # define function to display menu
    keyList = list(menuDict.keys())  # create list for keys in menu dictionary
    for index in range(len(keyList)):  # for loop to loop through key list
        value = menuDict[keyList[index]]  # get value from each key in menu dict
        print(keyList[index] + " -> " + value)  # print statements for each key:value set


def getUserInput(menuDict):  # define function to get user input
    userChoice = input("Choice: ")  # create variable for user input
    userChoice = userChoice.upper()  # set user input to uppercase
    keyList = list(menuDict.keys())  # get list of keys for menu dictionary
    while userChoice not in keyList:  # while loop for when user's choice is not in key list
        userChoice = input("Choice: ")  # ask user to reenter input
        userChoice = userChoice.upper()  # set input to uppercase
    return userChoice  # return user's choice


def printAllParks(parksList):  # define function to print all parks
    for index in range(len(parksList)):  # for loop to loop through parks list
        parkDict = parksList[index]  # create dictionary for every index in parks list
        # print statement with name, code, state, acres, and date established
        print(parkDict["Name"] + " (" + parkDict["Code"] + ")")
        print("\tLocation: " + parkDict["State"])
        print("\tArea: " + str(parkDict["Acres"]) + " acres")
        print("\tDate established: " + tasks.getDate(parkDict["Date"]))
        print()  # print new line for formatting


def getState():  # define function to get state
    stateInput = input("Enter a state: ")  # allow for user input of state
    while len(stateInput) != 2:  # while loop for when input does not have two characters
        print("Need the two letter abbreviation")  # print invalid statement
        stateInput = input("Enter a state: ")  # allow for another user input
    stateInput = stateInput.upper()  # set user input to uppercase

    return stateInput  # return user's input


def printParksInState(parksList):  # define function to print parks in one state
    state = getState()  # call getState function to get user input
    parkCount = 0  # create int variable for number of parks in a state and set to 0
    for index in range(len(parksList)):  # for loop to loop through parks list
        parkDict = parksList[index]  # create dictionary for every index in parks list
        if state in parkDict["State"]:  # if statement for if state fits value in park's "State" key
            parkCount += 1  # increment park count by 1
            # use park dict keys to print name, code, state, acres, and date established
            print(parkDict["Name"] + " (" + parkDict["Code"] + ")")
            print("\tLocation: " + parkDict["State"])
            print("\tArea: " + str(parkDict["Acres"]) + " acres")
            print("\tDate established: " + tasks.getDate(parkDict["Date"]))
            print()  # print new line
    if parkCount == 0:  # if statement for if park count is at 0
        # print statement for no parks in state
        print("There are no national parks in " + state + " or it is not a valid state")


def printLargestPark(parksList):  # define function to print largest park
    largestCode = tasks.getLargestPark(parksList)  # call function from tasks to get code from largest park
    for index in range(len(parksList)):  # for loop to loop through parks in parks list
        parkDict = parksList[index]  # create dictionary for each park in list
        # if statement for if code for largest park matches value in "Code" key for park dictionary
        if largestCode == parkDict["Code"]:
            # print statement with park's name, code, state, acres, date established, and description
            print(parkDict["Name"] + " (" + parkDict["Code"] + ")")
            print("\tLocation: " + parkDict["State"])
            print("\tArea: " + str(parkDict["Acres"]) + " acres")
            print("\tDate established: " + tasks.getDate(parkDict["Date"]))
            print("\tDescription: " + parkDict["Description"])


def printParksForSearch(parksList):  # define function to print parks in user search
    textSearch = input("Enter text for searching: ")  # allow for user search input
    searchCount = 0  # create int variable for number of results matching search entry
    for index in range(len(parksList)):  # for loop to loop through parks list
        parkDict = parksList[index]  # create dictionary for every index in parks list
        # if statement for if search shows up in "Code", "Description", and "Name" key:value sets
        if textSearch.upper() in parkDict["Code"] or textSearch.lower() in parkDict["Description"].lower() or \
                textSearch.lower() in parkDict["Name"].lower():
            searchCount += 1  # increment search count
            # print statement with park's name, code, state, acres, date established, and description
            print(parkDict["Name"] + " (" + parkDict["Code"] + ")")
            print("\tLocation: " + parkDict["State"])
            print("\tArea: " + str(parkDict["Acres"]) + " acres")
            print("\tDate established: " + tasks.getDate(parkDict["Date"]))
            print("\tDescription: " + parkDict["Description"])
            print()  # print new line
    if searchCount == 0:  # if statement for if search count equals to 0
        # print statement for no results matching user's search entry
        print("There are no national parks for the search title of '" + textSearch + "'.")


def printOldestPark(parksList):  # define function to print info on oldest park
    yearList = []  # create empty list to hold years of date established
    for index in range(len(parksList)):  # for loop to loop through parks list
        parkDict = parksList[index]  # create dictionary for every index in parks list
        dateList = parkDict["Date"].split("-")  # create list that splits date into year, month, and date
        yearList.append(dateList[0])  # append year of each park to yearList
    if len(yearList) == len(parksList):  # if statement for whether the yearList is the same length as the parkList
        yearList.sort()  # sort yearList in numerical order
        oldestDate = yearList[0]  # determine oldest date after sorting list
        for index in range(len(parksList)):  # for loop to loop through parks list another time to determine oldest park
            parkDict = parksList[index]  # create dictionary for every index in parks list
            if oldestDate in parkDict["Date"]:  # if statement for whether oldest date is in parkDict date key
                # print statement that shows name, code, location, acreage, date established, and description
                print(parkDict["Name"] + " (" + parkDict["Code"] + ")")
                print("\tLocation: " + parkDict["State"])
                print("\tArea: " + str(parkDict["Acres"]) + " acres")
                print("\tDate established: " + tasks.getDate(parkDict["Date"]))
                print("\tDescription: " + parkDict["Description"])
                print()  # print new line


def printStateWithMostParks(parksList):  # define function to print info on parks in state with most parks
    stateList = []  # create empty list to hold different states in file
    countList = []  # create empty list to hold park counts for different states
    countDict = {}  # create empty list to hold states as keys and its corresponding park counts as values
    for index in range(len(parksList)):  # for loop to loop through parks list
        parkDict = parksList[index]  # create dictionary for each index in parks list
        stateLine = parkDict["State"].strip()  # strip whitespace from "State" values
        lineList = stateLine.split(" & ")  # separate values by the & sign to consider parks in multiple states
        if lineList[0] not in stateList:  # if statement for whether park's state is not in state list yet
            stateList.append(lineList[0])  # append park's state into state list
    for stateIndex in range(len(stateList)):  # for loop to loop through indexes in state list
        parkCount = 0  # set int variable for park count as 0
        for parkIndex in range(len(parksList)):  # for loop to loop through each park in list
            parkDict = parksList[parkIndex]  # create dictionary for each park
            if stateList[stateIndex] in parkDict["State"]:  # if statement for whether state is in park's dictionary
                parkCount += 1  # increment for each time corresponding state appears in parkDict "State" value
        countList.append(parkCount)  # append count to count list after each state
    for countIndex in range(len(countList)):  # for loop to loop through counts in count list
        countDict[stateList[countIndex]] = countList[countIndex]  # set value in count dictionary for each state key
    countList.sort()  # sort count list in numerical order
    largestCount = countList[len(countList) - 1]  # create value that determines largest park count for all states
    for dictKey in countDict:  # for loop to loop through keys in countDict
        if largestCount == countDict[dictKey]:  # if statement for whether largest count equals the count for a state
            largestState = dictKey  # create variable that holds dictKey for largest state
    print("The state with the most parks is", largestState + "\n")  # print statement for state with most parks
    for index in range(len(parksList)):  # for loop to loop through parks list
        parksDict = parksList[index]  # create dictionary for each index in parks list
        if largestState in parksDict["State"]:  # if statement for whether largest state is in the states key for dict
            # print information on park including name, code, state, acreage, and date established
            print(parksDict["Name"] + " (" + parksDict["Code"] + ")")
            print("\tLocation: " + parksDict["State"])
            print("\tArea: " + str(parksDict["Acres"]) + " acres")
            print("\tDate established: " + tasks.getDate(parksDict["Date"]))
            print()  # print new line for formatting
