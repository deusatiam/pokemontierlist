### Imports ###
import numpy as np 
import pandas as pd 
from random import randrange



### Variables ###
# The filepath that the functions will default to in case they're not defined
default_filepath = "starter9.csv"
# The percentage of low-voted pokemon that will be potentially selected from
# High values increase selection randomness, low values promote low-voted pokemon to be selected
selection_ratio = 0.2    
# The ratios for the amounts of pokemon per tier.
# There must be 6 numbers and they must add up to 1
tier_ratios = [0.05,0.15,0.3,0.3,0.15,0.05]



### Functions ###
# This function sorts a given csv-file by either votes or score
# type can either be "Votes" or "Score"
def sort_csv(type = "Votes", csv = default_filepath):
    df = pd.read_csv(csv)

    # If sorting by votes, sort in ascending order
    if type == "Votes":         
        df = df.sort_values(type,axis=0,ascending=True,kind='quicksort')

    # If sorting by score, sort in descending order
    elif type == "Score":       
        df = df.sort_values(type,axis=0,ascending=False,kind='quicksort')

    # Error message
    else:                       
        print("Type in sort_csv incorrect.")

    df.to_csv(csv,index=False) 
    return



# This function generates a pair of pokemon id's, prioritizing pokemon with low votes
def get_pair(csv = default_filepath):
    df = pd.read_csv(csv)

    # Prioritize pokemon with less votes by sorting
    sort_csv("Votes", csv)

    # Find the highest index to choose from for voting
    limit = int(df.shape[0]*selection_ratio)

    # Minimum value for the limit for safety purposes
    if (limit < 5): limit = 5

    # Generate two different random integers within range of limit
    a = randrange(limit)            
    b = a
    while(b == a):
        b = randrange(limit)   
    
    # Determine the Id numbers for the two pokemon
    pokemon_a = df.iloc[a]['Id']    
    pokemon_b = df.iloc[b]['Id']

    return pokemon_a, pokemon_b



# This function votes for pokemon a, adding a vote to both pokemon and adding and 
# subtracting from their scores respectively
def vote(a, b, csv = default_filepath):
    df = pd.read_csv(csv)

    # Find the indices of the rows corresponding to the given pokemon id
    a_index = df[df['Id'] == a].iloc[0].name    
    b_index = df[df['Id'] == b].iloc[0].name

    # Update the votes
    df.loc[a_index, 'Votes'] += 1
    df.loc[b_index, 'Votes'] += 1

    # Update the scores
    df.loc[a_index, 'Score'] += 1
    df.loc[b_index, 'Score'] -= 1

    df.to_csv(csv,index=False)

    # Debugging printout
    print(df[df['Id'] == a].iloc[0][2] + " wins vs " + df[df['Id'] == b].iloc[0][2])
    return



# This function returns the sugimori filepath from a pokemon id
def get_sugimori(id, csv = default_filepath):
    df = pd.read_csv(csv)
    return df[df['Id'] == id].iloc[0]['Sugimori']



# This function returns the icon filepath from a pokemon id
def get_icon(id, csv = default_filepath):
    df = pd.read_csv(csv)
    return df[df['Id'] == id].iloc[0]['Icon']



# This function gets the name of a pokemon by it's id
def get_name(id, csv = default_filepath):
    df = pd.read_csv(csv)
    return df[df['Id'] == id].iloc[0]['Name']



# This function resets the scores and votes of each pokemon
def reset(csv = default_filepath):
    df = pd.read_csv(csv)
    df['Votes'] = 0
    df['Score'] = 0
    return



# This function returns the icon addresses for the tierlist
# Each tier has it's own subarray and the icons are in descending score order
def build_list(csv = "resources/starter9.csv"):
    # Sort the csv by score
    sort_csv(csv, "Score")
    df = pd.read_csv(csv)
    length = df.shape[0]
    tier_nums = []

    # Calculate the amount of pokemon per tier
    # The number of pokemon is going to be variable throughout development, so we'll 
    # calculate the number of pokemon in each tier each time the page is loaded for now
    for ratio in tier_ratios:
        # Make sure there's at least one pokemon per tier
        num = max(1,int(length*ratio))
        tier_nums.append(int(num))

    # Double check that the total number of pokemon is correct
    tier_sum = 0
    for i in tier_nums:
        tier_sum += i

    # If the number of pokemon isn't correct, add the difference to B-tier
    # This is very inelegant, but this works for now
    if tier_sum < length:
        tier_nums[2] += length - tier_sum
    
    # Add the appropriate number of pokemon into each subarray
    pokemon_no = 0
    output = []
    for i in tier_nums:
        tier = []
        j = 0
        while j < i:
            tier.append(df.loc[pokemon_no, 'Icon'])
            pokemon_no += 1
            j += 1
        output.append(tier)

    return output