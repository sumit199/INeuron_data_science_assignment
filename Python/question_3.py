#Write a program, which would download the data from the provided link, and then read the data and convert
#that into properly structured data and return it in Excel format.


#Note :- i am getting connection error when trying to directly access link. so, i have dowloaded file

import pandas as pd
import json

import json
file = 'G:\INeuron_data_science_assignment\pokedex.json'
#reading json into dcitionary
f = open ( file , "r") 
data = json.loads(f.read())
#dictionary is inside the pokemon key so will we access it 
data = data['pokemon']

df = pd.DataFrame.from_records(data)

#dropping id column
df.drop('id', axis=1, inplace=True)

#filling null values and dropping
print(df.isnull().sum())
df['multipliers'] = df['multipliers'].fillna("").apply(list)

df['candy_count'] = df['candy_count'].fillna(value=0)

#df['spawn_time'] = df['spawn_time'].replace("N/A","NA")
#df = df.dropna(subset=['spawn_time'])
df = df.drop([131,143,144,145,149,150])


#converting multipliers to list of int
def  convert_to_int(list_of_numbers):
    result = [int(item) for item in list_of_numbers]
    return result

df['multipliers'] = df['multipliers'].apply(convert_to_int)

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



#convert to min and seconds
df['spawn_time'] = pd.to_datetime(df['spawn_time'], format="%M:%S")
df['spawn_time'] = df['spawn_time'].dt.time


df.reset_index(inplace=True)
#converting dataframe to excel file
df.to_excel('pokemon.xlsx')

f.close()

