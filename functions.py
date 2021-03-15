import numpy as np 
import pandas as pd 
from random import randrange

# This function sorts a given csv-file by either votes or score
def sort_csv(csv = "resources/starter9.csv", type = "Votes"):
    df = pd.read_csv(csv)

    # If sorting by votes, sort in ascending order
    if type == "Votes":         
        df = df.sort_values(type,axis=0,ascending=True,kind='quicksort')

    # If sorting by score, sort in descending order
    elif type == "Score":       
        df = df.sort_values(type,axis=0,ascending=False,kind='quicksort')

    # Error message
    else:                       
        print("Type in sortCsv incorrect.")

    df.to_csv(csv,index=False) 
    return



# This function generates a pair of pokemon id's, prioritizing pokemon with low votes
def get_pair(csv = "resources/starter9.csv"):
    df = pd.read_csv(csv)

    # Prioritize pokemon with less votes by sorting
    sort_csv(csv, "Votes")

    # Find the highest index to choose from for voting
    limit = int(df.shape[0]*0.2)

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
def vote(a, b, csv = "resources/starter9.csv"):
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
    return



# This function resets the scores and votes of each pokemon
def reset(csv = "resources/starter9.csv"):
    df = pd.read_csv(csv)
    df['Votes'] = 0
    df['Score'] = 0
    return