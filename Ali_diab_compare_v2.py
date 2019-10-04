import numpy as np
import pandas as pd

### The goals is to check if phone number match in the field 'estate_phone ' of dupro.csv and cent.csv and to create another file.csv with only the item of dupro.csv without the any item of the matching of ph-one n-umber but be careful because we can have in each field 2,3 or more number. We need to check each one with each one. If a number match we don't take the line. We keep only the line who don't any number of cent.csv doesn't match
new_dupro = pd.read_csv('AVPP_TEL.csv')
new_dupro.dropna(subset=['estate_phone'], inplace=True)
new_dupro['estate_phone'].fillna(0, inplace=True)

base_list = list(map(lambda x: x.split(','), new_dupro['estate_phone'].astype(str)))

for i in range(len(base_list)):
    while '' in base_list[i]:
        base_list[i].remove('')

base_list = [list(map(float, map(int,i))) for i in base_list]

s_list = []
common = []
for i in range(len(base_list)):
    base = base_list[i]
    for k in range(len(base_list)):
        for j in range(len(base)):
            if base[j] in base_list[k]:
                common.append(k+1)
       
    common = list(set(common))
    common.remove(i+1)
    if len(common) == 0:
        s_list.append('')
    else:
        s_list.append(common)
    common = []

# final_list = [list(map(int, lst)) for lst in s_list]


new_dupro['similarity_column'] = s_list
new_dupro['similarity_column'] = new_dupro['similarity_column'].str[0]
new_dupro.to_csv('new_dupro_v2.csv', index=False)



