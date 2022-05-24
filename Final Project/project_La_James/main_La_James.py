# James La, jbla@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Final Project
# main_La_James.py
# Description: Reads CSV file with information on national parks; sorts through file to get information that is
# displayed depending on user's choice
# Describe what this file does: Calls functions from tasks and interface for main function to get information depending
# on user's inputs

import tasks  # import tasks to incorporate into main
import interface  # import interface to incorporate into main


def main():  # define main function
    print("National Parks")  # print opening statement
    parksList = tasks.createListOfParks()  # call createListOfParks function from tasks to get parks list
    menuDict = interface.getMenuDict()  # call getMenuDict function from interface to get menu dictionary
    interface.displayMenu(menuDict)  # call displayMenu function from interface to display menu
    userChoice = interface.getUserInput(menuDict)  # call getUserInput function from interface to get user's choice
    while userChoice != "Q":  # while loop for when user's choice is not Q (quit)
        # if-elif-else statement depending on user's choice
        if userChoice == "A":
            interface.printAllParks(parksList)  # call printAllParks function from interface to print info on all parks
        elif userChoice == "B":
            # call printParksInState function from interface to print info on states in user's park of choice
            interface.printParksInState(parksList)
        elif userChoice == "C":
            # call printLargestPark function from interface to print info on largest park
            interface.printLargestPark(parksList)
        elif userChoice == "D":
            # call printParksForSearch function from interface to print info on parks that are included in user's search
            interface.printParksForSearch(parksList)
        elif userChoice == "E":
            interface.printOldestPark(parksList)
        elif userChoice == "F":
            interface.printStateWithMostParks(parksList)
        else:
            print("Invalid input.")  # print statement for all invalid inputs
        print()  # print new line for formatting
        interface.displayMenu(menuDict)  # call displayMenu function from interface to show menu for another user input
        # call getUserInput function from interface to get another user input
        userChoice = interface.getUserInput(menuDict)


main()  # call main function
