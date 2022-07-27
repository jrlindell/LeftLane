import json
import requests

# gets company names associated with your Similarweb profile
def companies(api_key):
    '''
    Output: Returns the IDs and names of the custom Companies associated with your user, as defined on the Similarweb platform.
    '''
    url = "https://api.similarweb.com/v1/company/traffic-and-engagement/describe?api_key=" + api_key
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    return data

# get total traffic metrics from inputted company ids
'''
Output: Historical data goes back 24 months, depending on your subscription.
'''
def total_traffic(api_key, company_id, country, start_date, end_date, main_domain_only, granularity, metrics):
    url = "https://api.similarweb.com/v1/company/" + company_id + "/total-traffic-and-engagement/query?api_key=" + api_key + \
    "&country=" + country + "&start_date=" + start_date + "&end_date=" + end_date + "&main_domain_only=" + main_domain_only + \
    "&granularity=" + granularity + "&metrics=" + metrics
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    return data
