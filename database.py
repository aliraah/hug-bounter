import os
from dotenv import load_dotenv
import streamlit as st
from pymongo import MongoClient
from pandas import DataFrame
import requests
import datetime

#load_dotenv(".env")
#CONNECTION_STRING = os.getenv("CONNECTION_STRING")

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   #CONNECTION_STRING = ""
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['hug-bounty']
  

def collection_count(collection):
   dbname = get_database()
   collection = dbname[f'{collection}']
   
   entries = collection.find({})
   empty_list = []
   
   for i in entries:
       empty_list.append(1)
   return(len(empty_list))

@st.cache_data
def read_collection(collection):
    dbname = get_database()

    entries = []

    if collection == 'HackerOne':
        collection = dbname['HackerOne']
        for i in collection.find({}):
            data_dict = {}
            data_dict['Platform'] = i['platform']
            data_dict['Title'] = i['title']
            data_dict['Scope'] = i['scope']
            try:
               data_dict['Last Update'] = i['Last Update']
            except:
               pass
            entries.append(data_dict)

        df = DataFrame(entries)
        return(df)
        
    else:
        collection = dbname[f'{collection}']
        for i in collection.find({}):
            data_dict = {}
            data_dict['platform'] = i['platform']
            data_dict['title'] = i['title']
            data_dict['description'] = i['description']
            data_dict['scope'] = i['scope']
            try:
               data_dict['Last Update'] = i['Last Update']
            except:
               pass
            entries.append(data_dict)

    df = DataFrame(entries)
    return(df)


def read_programs(collection):
   dbname = get_database()
   collection = dbname[f'{collection}']

   programs = []

   for i in collection.find({}):
      programs.append(i['title'])

   return(programs)


def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


def update_collection(collection):
   dbname = get_database()
   
   now = datetime.datetime.now()

   if collection == 'YesWeHack':
      collection = dbname['YesWeHack']

      url = 'https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/yeswehack.json'
      r = requests.get(url)
      data = r.json()

      for i in data:
         collection.update_many({"title":i["title"]},{"$set": {"scope":i["scopes"], "description":i["business_unit"]["description"], "Last Update":now}})

   elif collection == 'Intigriti':
      collection = dbname['Intigriti']

      url = 'https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/intigriti.json'
      r = requests.get(url)
      data = r.json()

      for i in data:
         collection.update_many({"title":i["name"]},{"$set": {"scope":i["domains"], "description":i["description"], "Last Update":now}})

   elif collection == 'Bugcrowd':
      collection = dbname['Bugcrowd']

      url = 'https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/bugcrowd.json'
      r = requests.get(url)
      data = r.json()

      for i in data:
         collection.update_many({"title":i["name"]},{"$set": {"scope":i["target_groups"], "description":i["tagline"], "Last Update":now}})

   elif collection == 'HackerOne':
      collection = dbname['HackerOne']

      url = 'https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/hackerone.json'
      r = requests.get(url)
      data = r.json()

      for i in data:
         collection.update_many({"title":i["attributes"]["name"]},{"$set": {"scope":i["relationships"]["structured_scopes"], "Last Update":now}})



def manual_update(platform, title, description, scope):
    dbname = get_database()
    collection = dbname[f'{platform}']
    now = datetime.datetime.now()

    data_dict = {}
    data_dict['platform'] = platform.lower()
    data_dict['title'] = title
    data_dict['description'] = description

    # -- Get scope value as string and turn it into an object to be displayable along with other results -- #
    scope = scope.split(',')
    scope_as_list = []
    count = 0
    for i in scope:
      data_dict2 = {}
      data_dict2[str(count)] = i
      count+=1
      scope_as_list.append(data_dict2)

    data_dict['scope'] = scope_as_list
    data_dict['Last Update'] = now
    
    collection.insert_one(data_dict)



def delete_record(collection, title):
    dbname = get_database()
    collection = dbname[f'{collection}']
    
    query = {"title":f"{title}"}

    result = collection.find_one(query)
    
    if result:
        collection.delete_one(query)
        msg = title + ' successfully removed!'
        st.success(msg)
    else:
        err = 'Program not found: ' + title
        st.error(err)
