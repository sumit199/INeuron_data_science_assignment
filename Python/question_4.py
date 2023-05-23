#Write a program to download the data from the link given below and then read the data and convert the into
#the proper structure and return it as a CSV file

#Link - https://data.nasa.gov/resource/y77d-th95.json

import pandas as pd

data = pd.read_json("https://data.nasa.gov/resource/y77d-th95.json")

#converting dict to dataframe
df = pd.DataFrame(data)

# normaling geolocation column to get dict data inside it 
df2 = pd.json_normalize(df['geolocation'])

df['coordinates'] = df2['coordinates']

#dropping columns
df.drop(df.columns[[5,9,10,11]],axis=1,inplace=True)

#converting data types of column
convert_dict = {'name': str,
                 'nametype':str,
                 'recclass':str,
                 'mass':float,
                 'reclat':float,
                 'reclong': float,
                }
df = df.astype(convert_dict)

#converting to datetime
df['year'] = pd.to_datetime(df['year'],format='%Y-%m-%dT%H:%M:%S.%f', errors = 'coerce')

df = df.set_index('id')

print(df.isnull().sum())
df.dropna(inplace=True)

#conver cordinates to list of int
def  remove_brackets_num(list_of_numbers):
    result = [int(item) for item in list_of_numbers]
    return result

df['coordinates'] = df['coordinates'].apply(remove_brackets_num)


print(df.info())
#saving to csv file
df.to_csv('po.csv')
