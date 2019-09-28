
import numpy as np
import pandas as pd



# ### The goals is to check if phone number match in the field 'estate_phone ' of dupro.csv and cent.csv and to create another file.csv with only the item of dupro.csv without the any item of the matching of ph-one n-umber but be careful because we can have in each field 2,3 or more number. We need to check each one with each one. If a number match we don't take the line. We keep only the line who don't any number of cent.csv doesn't match


cent = pd.read_csv('cent.csv')
dupro = pd.read_csv('dupro.csv') # This is what we want, minus the common numbers of cent


cent['estate_phone'].fillna('0', inplace=True)
dupro['estate_phone'].fillna('0', inplace=True)


#Creating list of all the phone number of cent and dupro. Also, creating set of numbers in cent, as it's just for checking. 
ce_list = list(set(np.concatenate(list(map(lambda x: str(x).split(','), cent['estate_phone'].values))).ravel()))
du_list = list(map(lambda x: str(x).split(','), dupro['estate_phone'].values))


#Converting all possible values of ce_list and du_list to float, as it's faster in comparison. 
for i in range(len(ce_list)):
    try:
        ce_list[i] = float(ce_list[i])
    except:
        print(ce_list[i])
        
for i in range(len(du_list)):
    for j in range(len(du_list[i])):
        try:
            du_list[i][j] = float(du_list[i][j])
        except:
            new = du_list[i][j]

#Keeping all the numbers of du_list that are not in ce_list
keep = []
for i in range(len(du_list)):
    for j in range(len(du_list[i])):
        if du_list[i][j] in ce_list:
            break
        if j == len(du_list[i]) - 1:
            keep.append(i)
        
            

# Creating that new dataframe, which has all the rows of whose estate_phone are not in cent's estate_phone
new_dupro = dupro.loc[keep]


new_dupro.to_csv('new_dupro.csv')

