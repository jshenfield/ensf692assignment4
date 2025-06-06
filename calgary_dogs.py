# calgary_dogs.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import re
import numpy as np
import pandas as pd
print(pd.__version__)

######################

# This function is meant to add spaces to camelCase/MixedCase inputs
def addspaces(a):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', a) # inspired by chatgpt

# This function is meant to normalize the input for comparison with the dog breeds in the dataframe
# parameter a: input string to be normalized
# returns: normalized version of a
def normalizestring(a):
    a = addspaces(a)
    a = a.lower()
    return(a)

# This function takes in a dataframe, prompts for userinput, and then returns a new dataframe of selected data (dog breed)
# It continues to loop until a proper dog breed is inputted.
# parameter dataframe: input dataframe
# returns the data in dataframe where the breed is equal to the input (slices it)
def extractdogbreed(dataframe):
    while True: # loops until valid input is received
        userinput = input("Please enter a dog breed: ") # ask for input

        userinput = normalizestring(userinput) # normalizes the input string
        datalower = dataframe['Breed'].str.lower() # lowercase the breeds for comparison

        if userinput in datalower.values:
            return(dataframe[datalower == userinput]) # return data in dataframe where datalower is equal to userinput
        else:
            print("Dog breed not found in data. Please try again.")
            #raise KeyError("Dog breed not found in data. Please try again.")

def main():

    # Import data here

    imported_data = pd.read_excel("CalgaryDogBreeds.xlsx")
    #print(imported_data)
    data = pd.DataFrame(imported_data)
    #print(data['Breed'])
    
    
    print("ENSF 692 Dogs of Calgary")

    # User input stage
    dogbreed = extractdogbreed(data)
    #print(dogbreed)


    # Data analysis stage

    dogbreedname = dogbreed['Breed'].values[1] # extracts just the name of the dog breed for printing purposes

    print("The ", dogbreedname, "was found in the top breeds for the years: ", dogbreed['Year'].unique())
    print("There have been ", sum(dogbreed['Total']), dogbreedname, "dogs registered in total.")

    # 2021 calculations
    dogbreed2021 = (dogbreed[dogbreed['Year'].values == 2021]) # extracts chosen dog breed 2021 data
    dogbreed2021total = sum(dogbreed2021['Total']) # extracts sum of chosen dog breed for 2021
    alldogbreed2021 = (data[data['Year'].values == 2021]) # extracts sum of all dog breeds for 2021
    alldogbreed2021total = sum(alldogbreed2021['Total'])
    dogbreed2021percent = (dogbreed2021total/alldogbreed2021total) # calculate the percentage of dog breeds

    # 2022 calculations
    dogbreed2022 = (dogbreed[dogbreed['Year'].values == 2022]) # extracts chosen dog breed 2022 data
    dogbreed2022total = sum(dogbreed2022['Total']) # extracts sum of chosen dog breed for 2022
    alldogbreed2022 = (data[data['Year'].values == 2022]) # extracts sum of all dog breeds for 2022
    alldogbreed2022total = sum(alldogbreed2022['Total'])
    dogbreed2022percent = (dogbreed2022total/alldogbreed2022total) # calculate the percentage of dog breeds

    # 2023 calculations
    dogbreed2023 = (dogbreed[dogbreed['Year'].values == 2023]) # extracts chosen dog breed 2023 data
    dogbreed2023total = sum(dogbreed2023['Total']) # extracts sum of chosen dog breed for 2023
    alldogbreed2023 = (data[data['Year'].values == 2023]) # extracts sum of all dog breeds for 2023
    alldogbreed2023total = sum(alldogbreed2023['Total'])
    dogbreed2023percent = (dogbreed2023total/alldogbreed2023total) # calculate the percentage of dog breeds
    
    # Overall calculations
    dogbreedtotal = sum(dogbreed['Total'])
    overallbreedtotal = sum(data['Total'])
    overallbreedpercent = (dogbreedtotal/overallbreedtotal)

    print("The ", dogbreedname, "was", round(dogbreed2021percent * 100, 6), "% of top breeds in 2021.")
    print("The ", dogbreedname, "was", round(dogbreed2022percent * 100, 6), "% of top breeds in 2022.")
    print("The ", dogbreedname, "was", round(dogbreed2023percent * 100, 6), "% of top breeds in 2023.")
    print("The ", dogbreedname, "was", round(overallbreedpercent * 100, 6), "% of top breeds across all years.")


    #print("Most popular month(s) for ", dogbreedname, " dogs:",       )

if __name__ == '__main__':
    main()
