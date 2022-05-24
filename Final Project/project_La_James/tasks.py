# James La, jbla@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Final Project
# tasks.py
# Description: Reads CSV file with information on national parks; sorts through file to get information that is
# displayed depending on user's choice
# Describe what this file does: Sets foundation for project by reading through CSV file and creating base variables that
# will be implemented throughout the entire project


def createListOfParks(fileName="national_parks.csv"):  # define function to create list of parks
    parksList = []  # create an empty list for parks
    fileRead = open(fileName, "r")  # open file for reading
    headerLine = fileRead.readline()  # skip header line in reading
    for line in fileRead:  # for loop to loop through file lines
        line = line.strip()  # strip line of whitespace
        parkLine = line.split(",")  # split string into list
        parkDict = {}  # create park dictionary for each line
        for index in range(len(parkLine)):  # for loop to loop through each park line
            # assign dictionary key:value set for each index in park line
            parkDict["Code"] = parkLine[0]
            parkDict["Name"] = parkLine[1]
            parkDict["State"] = parkLine[2]
            parkDict["Acres"] = int(parkLine[3])
            parkDict["Latitude"] = parkLine[4]
            parkDict["Longitude"] = parkLine[5]
            parkDict["Date"] = parkLine[6]
            parkDict["Description"] = ",".join(parkLine[7:])  # use join to connect the entire description
        parksList.append(parkDict)  # append park info to parks list
    fileRead.close()  # close file for reading

    return parksList  # return parks list


def getDate(dataStr):  # define function to reformat date
    dateList = dataStr.split("-")  # split date into list
    # if-elif-else statement (branching) through months in numbers and convert them to corresponding name
    if dateList[1] == "01":
        dateList[1] = "January"
    elif dateList[1] == "02":
        dateList[1] = "February"
    elif dateList[1] == "03":
        dateList[1] = "March"
    elif dateList[1] == "04":
        dateList[1] = "April"
    elif dateList[1] == "05":
        dateList[1] = "May"
    elif dateList[1] == "06":
        dateList[1] = "June"
    elif dateList[1] == "07":
        dateList[1] = "July"
    elif dateList[1] == "08":
        dateList[1] = "August"
    elif dateList[1] == "09":
        dateList[1] = "September"
    elif dateList[1] == "10":
        dateList[1] = "October"
    elif dateList[1] == "11":
        dateList[1] = "November"
    else:
        dateList[1] = "December"
    datePrint = dateList[1] + " " + dateList[2] + ", " + dateList[0]  # reformat dates for printing

    return datePrint  # return reformatted date


def getLargestPark(parksList):  # define function to determine largest park
    acresList = []  # create list for acres of parks
    largestCode = ""  # create variable that holds code for largest park
    for index in range(len(parksList)):  # for loop to loop through list of park dictionaries
        parkDict = parksList[index]  # create dictionary variable for each park
        acresList.append(parkDict["Acres"])  # get value of "Acres" key and append to list of acres
        acresList.sort()  # sort list in alphanumeric order
        largestAcres = acresList[len(acresList) - 1]  # determine largest acreage after sorting list
        if largestAcres == parkDict["Acres"]:  # if statement to determine which key holds largest acreage
            largestCode = parkDict["Code"]  # get code for corresponding key

    return largestCode  # return code for key with largest acreage
