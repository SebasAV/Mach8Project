# -*- coding: utf-8 -*-
"""
This is the Sebastian Aponte Vivas sample project.

This function allows the user to enter an integer and
print a list with the names of all pairs of NBA players 
whose height in inches adds up to the integer.
---------------------------------------------------------
USE:
In command prompt type:
    python test.py <Integer>
    
    example:
        python test.py 139
        
        or
        
        python test.py(139)

---------------------------------------------------------
RETURN:
The function will return a list with the names of all
pairs of NBA players whose height in inches adds up to
the entered integer.
"""
import sys
import requests as req
import itertools

def findPairs(data, integerInput):
    # Define the players list to be returned
    playerList = []
    
    # Find all possible combinations
    numComb = list(itertools.combinations(data, 2))
    
    # Execute the query
    query = list(filter(lambda player: int(player[0]['h_in'])+int(player[1]['h_in']) == integerInput, numComb))

    # Store the found pairs of players on a list
    playerList = [[playerInfo[i].get('first_name') + ' ' + playerInfo[i].get('last_name') for i in range(2)] for playerInfo in query]    
    
    # Print the players in console
    if len(playerList) >= 1:
        for playerInfo in playerList: print('-{}    {}'.format(playerInfo[0], playerInfo[1]))
    else:
        # In case no matches sum the input quantity
        print('\nNo matches found\n')
    
    # Return the list of found pairs of players
    return playerList

def inputValidations(arguments):
    # Check if more than one argument was entered, else return the input as an integer
    if len(arguments) > 2:
        print('\nInvalid number of arguments: Input should have only one argument, ex. 139\n')
        sys.exit()
    else:
        # Try to conver the user input to integer, if not possible print a message to the user
        try:
            int(arguments[1])
            return int(arguments[1])
        except:
            print('\nInvalid input: Input should be an integer, ex. 139\n')

def main():    
    # Execute the get request
    jsonResponse = req.get('https://mach-eight.uc.r.appspot.com/')
    
    # Get the json values of the response
    playersJson = jsonResponse.json()['values']
    
    # Validate that the user input has been correctly entered
    userinput = inputValidations(sys.argv)

    # If the user input is not empty search for the pairs of players
    if userinput is not None:
        findPairs(playersJson, userinput)
    
if __name__ == '__main__':
    main()
        