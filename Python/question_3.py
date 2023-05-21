#Write a program, which would download the data from the provided link, and then read the data and convert
#that into properly structured data and return it in Excel format.


#Note :- i am getting connection error when trying to directly access link. so, i have dowloaded file

import pandas as pd
import json
from datetime import datetime

file = 'pokedex.json'
#reading json into dcitionary
f = open ( file , "r") 
data = json.loads(f.read())
#dictionary is inside the pokemon key so will we access it 
data = data['pokemon']
#normalize the dictionary as it contain multilevel dictionary
dict_data = pd.json_normalize(data, sep=',')
#converting dict to dataframe
df = pd.DataFrame(dict_data)
#dropping id column
df.drop('id', axis=1, inplace=True)

#drop null values
print(df.isnull().sum())
df.dropna(inplace=True)

#remove brackets from strings from type column
def  remove_brackets_str(list_of_strings):
    result = ', '.join(list_of_strings)
    return result

df['type'] = df['type'].apply(remove_brackets_str)

#converting multipliers to list of int
def  remove_brackets_num(list_of_numbers):
    result = [int(item) for item in list_of_numbers]
    return result

df['multipliers'] = df['multipliers'].apply(remove_brackets_num)

#dropping char linke m and kg from  height and weight column so we convert it 
df["height"] = df["height"].str.replace("m","")
df["weight"] = df["weight"].str.replace("kg","")

convert_dict = {'num':int,
                'name': str,
                 'img':str,
                 'type':str,
                 'height':float,
                 'weight':float,
                 'candy': str,
                 'candy_count':int,
                 'spawn_chance':float,
                 'avg_spawns':int,
                }
df = df.astype(convert_dict)



#conver to min and seconds
df['spawn_time'] = pd.to_datetime(df['spawn_time'], format='%H%M:%S')

df['minute'] = df['spawn_time'].dt.minute
df['second'] = df['spawn_time'].dt.second
df['spawn_time'] = (pd.to_datetime(df['minute'].astype(str) + ':' + df['second'].astype(str), format='%M:%S')
          .dt.time)

df.drop(df[['minute','second']],axis=1,inplace=True)

#converting dataframe to excel file
df.to_excel('pokemon.xlsx')

f.close()

