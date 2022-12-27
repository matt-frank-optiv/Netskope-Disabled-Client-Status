#!/usr/bin/env python
# coding: utf-8

# In[9]:


#requires dotenv to store tenant URL and API Key in local .env file

from dotenv import load_dotenv
import os
import requests
import json
import time
import datetime
from datetime import datetime 
import csv

#Load variables/secrets from .env
load_dotenv()

#number of days to return results for from the JSON response
range = 7

#query NSKP v1 API for client data.  This will return agents that have been disabled, whether by the user, system shutdown, etc.  
payload = {'token': os.environ.get('v1_api_key'), 'query': 'last_event.status eq \'Disabled\''}
r = requests.post(f'https://{os.environ.get("ns_tenant")}.goskope.com/api/v1/clients', verify=True, json=payload)

response = json.loads(r.content)
clients = response['data']

#outputs for JSON results to be read into.
disabled = list()
disabled_reason = dict()


#create CSV header rows
disabled.insert(0,['hostname', 'last_event', 'agent_status', 'user_name', 'last_event_date'])    

#for each client returned in the JSON result, loop through results to find the devices that have the Netskope ageent disabled and append to the list of devices that match the
    #below criteria based on 'range' noted above. 
for client in clients:
     if client['attributes']['last_event']['timestamp'] >= time.time() - 86400 * range:
            disabled.append([client['attributes']['_id'], client['attributes']['last_event']['event'], client['attributes']['last_event']['status'], client['attributes']['users'][0]['username'], datetime.fromtimestamp(client['attributes']['last_event']['timestamp'])])            

#write results to .csv              
file = open('results.csv', 'a+') 
with file:
    write = csv.writer(file)
    write.writerows(disabled)
    





# In[ ]:





# In[ ]:





# In[ ]:




