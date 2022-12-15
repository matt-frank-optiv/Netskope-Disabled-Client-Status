# Netskope-Client-Status

Uses the Netskope v1 of the API in order to retrieve agents that are disabled. 

Requires:
- python 3.x
- dotenv (pip3 install dotenv)
- Juypter Lab/Notebook (optional) 

Usage:

Create .env file in directory with the below values
- ns_tenant = {your netskope tenant prefix (ex. tenant1) for tenant1.goskope.com
- v1_api_key = {v1 API key from the Netskope tenant}

Change the 'Range' value to retrieve results that have a last event date of greater than 7 days (default)


Output: 

Running the script will export a results.csv file which contains a list of the Netskope Agents that are disabled, along with the username, last event, and last event timestamp.
