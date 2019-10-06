import numpy as np
import pandas as pd

#Importing dataset
new_dupro = pd.read_csv('AVPP_immo.csv')
new_dupro['estate_phone'].fillna(0, inplace=True)

base_list = list(map(lambda x: x.split(','), new_dupro['estate_phone'].astype(str)))

#Removing all blank characters in numbers
for i in range(len(base_list)):
    while '' in base_list[i]:
        base_list[i].remove('')

#Converting all numbers from string format to float
base_list = [list(map(float, map(int,i))) for i in base_list]

# Making set of all the shared numbers in the dataframe
s_list = []
common = []
for i in range(len(base_list)):
    base = base_list[i]
    for k in range(len(base_list)):
        for j in range(len(base)):
            if base[j] in base_list[k]:
                common.append(k)
       
    common = list(set(common))
    if len(common) == 0:
        s_list.append('')
    else:
        s_list.append(common)
    common = []

    
safe = s_list.copy()

c_list = safe.copy()
s_list = safe.copy()

#Now assigning a unique id to all the rows based on length. As only the rows that share number with some other row have length of s_list greater than 1
count = 1000
visited = set()

for i in range(len(s_list)):
    if i in visited:
        pass
    else:
        if len(s_list[i])>1:
            for j in range(len(s_list[i])):
                c_list[s_list[i][j]] = count
                visited.add(s_list[i][j])
            count+=1
        else:
            c_list[i] = ''

# Just making a new column with the new c_list as similarity_column
new_dupro['similarity_column'] = c_list
new_dupro['similarity_column'] = new_dupro['similarity_column']
new_dupro.to_csv('new_dupro_v2.csv')


