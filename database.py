import os
from dotenv import load_dotenv
from deta import Deta
import requests

#--Load the environment variables--#
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

#---Initialize with project key---#
deta = Deta(DETA_KEY)

#---This how to connect to or create a database---#
db = deta.Base("Hunt-DB")



def fetch_all_records():
	#---Returns a dict of all data---#
	res = db.fetch()
	return res.items


def delete_all_records():
    response = db.fetch(query={})  #---Fetch all documents---#

    #---Delete each document---#
    for item in response.items:
        db.delete(item['key'])



def update_yeswehack():
    #---Get data from github and parse with json---# 
    url = "https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/yeswehack.json"
    r = requests.get(url)
    data = r.json()

    data_list = []
    
    for i in data:
        #---Put desired data from the json file into the data_list---#
        data_dict = {}
        data_dict['platform'] = "YesWeHack"
        data_dict['title'] = i['title']
        data_dict['description'] = i['business_unit']['description']
        data_dict['scope'] = i['scopes']
        #data_dict['scope_count'] = i['scopes_count']
        #data_dict['reports_count'] = i['reports_count']
        #data_dict['min_bounty'] = i['bounty_reward_min']
        #data_dict['max_bounty'] = i['bounty_reward_max']
        #data_dict['currency'] = i['business_unit']['currency']
        data_list.append(data_dict)

    #---Insert each item on data_list into the DB---#
    for item in data_list:
        db.put({
            'platform': item['platform'],
            'key': item['title'],
            'description': item['description'],
            'scope': item['scope']
            #'scope_count': item['scope_count'],
            #'reports_count': item['reports_count'],
            #'min_bounty': item['min_bounty'],
            #'max_bounty': item['max_bounty'],
            #'currency': item['currency']
        })

def retrieve_yeswehack():
    #---Define the query to retrieve rows where column('platform') equals target_value('YesWeHack')---#
    query = {'platform': 'YesWeHack'}

    #---Retrieve matching rows---#
    response = db.fetch(query=query)

    #--Return the matching rows---#
    return response.items

def retrieve_intigriti():
    #---Define the query to retrieve rows where column('platform') equals target_value('Intigriti')---#
    query = {'platform': 'Intigriti'}

    #---Retrieve matching rows---#
    response = db.fetch(query=query)

    #--Return the matching rows---#
    return response.items

def retrieve_bugcrowd():
    #---Define the query to retrieve rows where column('platform') equals target_value('Bugcrowd')---#
    query = {'platform': 'Bugcrowd'}

    #---Retrieve matching rows---#
    response = db.fetch(query=query) 
    
    """
    Problem:
    fetch() Retrieves a list of items matching a query. It will retrieve everything if no query is provided, up to a limit of 1 MB or 1000 items.
    """
    
    #--Return the matching rows---#
    return response.items


def update_intigriti():
    #---Get data from github and parse with json---# 
    url = "https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/intigriti.json"
    r = requests.get(url)
    data = r.json()

    data_list = []
    
    for i in data:
        #---Put desired data from the json file into the data_list---#
        data_dict = {}
        data_dict['platform'] = "Intigriti"
        data_dict['title'] = i['name']
        data_dict['description'] = i['description']
        data_dict['scope'] = i['domains']
        data_list.append(data_dict)

    #---Insert each item on data_list into the DB---#
    for item in data_list:
        db.put({
            'platform': item['platform'],
            'key': item['title'],
            'description': item['description'],
            'scope': item['scope']
            #'scope_count': item['scope_count'],
            #'reports_count': item['reports_count'],
            #'min_bounty': item['min_bounty'],
            #'max_bounty': item['max_bounty'],
            #'currency': item['currency']
        })


def update_bugcrowd():
    #---Get data from github and parse with json---# 
    url = "https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/bugcrowd.json"
    r = requests.get(url)
    data = r.json()

    data_list = []

    for i in data:
        #---Put desired data from the json file into the data_list---#
        data_dict = {}
        data_dict['platform'] = "Bugcrowd"
        data_dict['title'] = i['name']
        data_dict['description'] = i['tagline']
        data_dict['scope'] = i['target_groups']
        data_list.append(data_dict)
    
    #---Insert each item on data_list into the DB---#
    for item in data_list:
        db.put({
            'platform': item['platform'],
            'key': item['title'],
            'description': item['description'],
            'scope': item['scope']
        })


