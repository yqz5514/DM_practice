# %%------------------------------------------------------------------------------
# Question 1:
# Run the following code.
# 1- Explain what does it do.
# 2- What can be as an input to this function and what are the outputs.
# 3- Is there something wrong in this code (code logic). If no Why?, If yes, what is the fix?
# 4- The following code represent and algorithm. Write down the logic algorithm .
# %%------------------------------------------------------------------------------
def a(b, c):
    d = 0
    e = False

    while d < len(b) and e is False:
        if b[d] == c:
            e = True
        else:
            d = d + 1

    return e
print(a('Alex','d'))
#it is going to check if the letter c=''  is in the letters in b , if not it is going
# to go through the end of the sting to check, here we don't have d in Alex so it is going from A to x
# and then cause not founding d it is going to return false
#2 b is going to be the string and c should be the letter(string type) , the output is going to be True or False
#
#3 it is correct and working like Alex does not have 'd' then it would return
#false
# because it is running perfectly so there is not any logic problems with this code
#4 it is going to do the linear sreach and not even make the string half like the binary search so it is going to take some time
#so just start from the begining letter and continue to the last one
#which is super time consumeing





# %%------------------------------------------------------------------------------
# Question 2:
# Graphs are networks that have nodes connected by edges or arcs.
# In directed graphs, the relationship between nodes have a direction,
# and are called arcs, in not directed graphs, the connections have no
# direction and are names edges. Assume we have the following graph.
# A -> B
# A -> C
# B -> C
# B -> D
# C -> D
# D -> C
# E -> F
# F -> C
# 1- Assign the following graph to a meaningful python variable and explain why that is the best.
# 2- Write a function to find a path between two nodes.
# It takes a graph (variable in 1) and the start and end as input. It will return a list of nodes
# 3- Change question number 2 code to find all the paths between a given start and end.
# 4- Change question number 3 and finds the closest or shortest path between two given start and end node.
# %%------------------------------------------------------------------------------
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
#2
def navigate_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = navigate_path(graph, node, end, path)
            if newpath: return newpath
    return None
    navigate_path(graph, 'A', 'D')
    print(graph)



# %%------------------------------------------------------------------------------
import pandas as pd
import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# %%------------------------------------------------------------------------------
# %%------------------------------------------------------------------------------
# Question 3:
import pandas as pd
# Consider the following Python dictionary data and Python list labels, Answer the following questions
# 1- Create a DataFrame df from this dictionary data which has the index labels.
df = pd.DataFrame(data,labels)
# 2- Display a summary of the basic information about this DataFrame and its data.
print(df.info())
# 3- Return the first 3 rows of the DataFrame df.
print(df.head(3))
# 4- Select just the 'animal' and 'age' columns from the DataFrame df
print(df.iloc[0,1])
# 5- Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].

print(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])

# 6- Select only the rows where the number of visits is greater than 3.
print(df[df['visits'] > 3])
# 7- Select the rows where the age is missing, i.e. is NaN.
print(df[df['age'].isnull()])
# 8- Select the rows where the animal is a cat and the age is less than 3.
print(df[(df['animal'] == 'cat') & (df['age'] < 3)])
# 9- Select the rows the age is between 2 and 4 (inclusive).
print(df[df['age'].between(2, 4)])
# 10- Change the age in row 'f' to 1.5.
df.loc['f', 'age'] = 1.5
# 11- Calculate the sum of all visits (the total number of visits).
print(df['visits'].sum())
# 12- Calculate the mean age for each different animal in df.
print(df.groupby('animal')['age'].mean())
# 13- Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame.
df.loc['k'] = [5.5, 'dog', 'no', 2]

# and then deleting the new row...

df = df.drop('k')
# 14- Count the number of each type of animal in df.
print(df['animal'].value_counts())
# 15- Sort df first by the values in the 'age' in decending order, then by the value in the 'visit' column in ascending order.
print(df.sort_values(by=['age', 'visits'], ascending=[False, True]))
# 16- The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes'
df['priority'] = df['priority'].map({'yes': True, 'no': False})
print(df)
# should be True and 'no' should be False.
# 17- In the 'animal' column, change the 'snake' entries to 'python'.
df['animal'] = df['animal'].replace('snake', 'python')
print(df)
# 18- For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column
# is a number of visits and the values are the mean ages (hint: use a pivot table).
#it should work but because of the error I  just comment it.you should un comment the next line.
#uncomment the next line please
#df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')



# %%------------------------------------------------------------------------------
# Question 4:
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of
# congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import sys
user1 = input("What's your name?")
user2 = input("what is  your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))








# %%------------------------------------------------------------------------------