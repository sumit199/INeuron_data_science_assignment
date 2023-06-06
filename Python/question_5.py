#Write a program to download the data from the given API link and then extract the following data with
#proper formatting
#http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes

import pandas as pd 
import requests
from datetime import datetime


link = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'

#method to get data from link in json format
def data_request(link):
    
    result = requests.get(link)
    result.status_code
    if result.status_code == 200:
        data = result.json()
        print("\n Data is retrieved sucessfully. \n")
        
        #data = pd.json_normalize(data)
        df = pd.DataFrame.from_dict(data['_embedded'])
        df.to_json('tvmazedata.json') 

        #print(df.info())
    else:
        print("\n ERROR")

#data_request(link)

#reading json file
df1 = pd.read_json('tvmazedata.json')

#getting episodes data from json file and normalizing it
df2 = pd.json_normalize(df1['episodes'])

#saving in csv format
df2.to_csv('tvmazedata.csv')

df3 = pd.read_csv('tvmazedata.csv', index_col=False)

#dropping columns
df3.drop(df3.columns[[0,9,15,16]], axis=1,inplace=True)

#renaming columns
df3.rename(columns = 
        {'rating.average':'average_rating','image.medium':'medium_image_link','image.original':'original_image_link'},
          inplace = True)
#converting airdate to datetime
df3['airdate'] = pd.to_datetime(df3['airdate'])

#method to airtime to 12hr format
def time_convert(time_to_convert):
     return datetime.strptime(time_to_convert, "%H:%M").strftime('%I:%M %p')

df3['airtime'] = df3['airtime'].apply(time_convert)

#converting all the data types of columns
convert_dict ={
                'url':str,
                'name':str,
                'season':int,
                'number':int,
                'type':str,
                'runtime':float,
                'average_rating':float,
                'summary':str,
                'medium_image_link':str,
                'original_image_link':str
               }

df3 = df3.astype(convert_dict)

#removing html tags from summary
df3['summary'] = df3['summary'].str.replace(r'<[^<>]*>', '', regex=True)

print(df3.info())

df3.to_csv('maze.csv')

