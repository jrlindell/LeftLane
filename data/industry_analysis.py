import json
import requests

def top_sites_desktop(api_key, industry, start_date, end_date, country, get_all):
    '''
    Output: Top sites based on Desktop web traffic in a given category
    input:
        api_key = api_key for similarweb
        industry = industry you want. can be "$All" if you want all (categories found at https://api.similarweb.com/v1/TopSites/categories)
        start_date = have to be set as the previous month (first day of last month)
        end_date = have to be set as the previous month (last day of last month)
        country = two letter country, all lowercase (ex. us, gb)
        get_all = if you want to get all 100 pages from the api, put true, otherwise, it will get top 100 entries
    '''
    data = []
    if get_all == 'True':
        for i in range(1, 100):
            url = "https://api.similarweb.com/v1/website/" + industry + "/topsites/desktop?api_key=" + api_key + \
                "&start_date=" + start_date + "&end_date=" + end_date + "&country=" + country + "&format=json&page=" + i
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
        
            data.extend(response.json())
    else:
        url = "https://api.similarweb.com/v1/website/" + industry + "/topsites/desktop?api_key=" + api_key + \
                "&start_date=" + start_date + "&end_date=" + end_date + "&country=" + country + "&format=json&page=1"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
    
    return data

def top_sites_mobile(api_key, industry, start_date, end_date, country, get_all):
    '''
    Output: Top sites based on mobile web traffic in a given category
    input:
        api_key = api_key for similarweb
        industry = industry you want. can be "$All" if you want all (categories found at https://api.similarweb.com/v1/TopSites/categories)
        start_date = have to be set as the previous month (first day of last month)
        end_date = have to be set as the previous month (last day of last month)
        country = two letter country, all lowercase (ex. us, gb)
        get_all = if you want to get all 100 pages from the api, put true, otherwise, it will get top 100 entries
    '''
    data = []
    if get_all == 'True':
        for i in range(1, 100):
            url = "https://api.similarweb.com/v1/website/" + industry + "/topsites/mobile?api_key=" + api_key + \
                "&start_date=" + start_date + "&end_date=" + end_date + "&country=" + country + "&format=json&page=" + i

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            
            data.extend(response.json())
        else:
            url = "https://api.similarweb.com/v1/website/" + industry + "/topsites/mobile?api_key=" + api_key + \
                "&start_date=" + start_date + "&end_date=" + end_date + "&country=" + country + "&format=json&page=1"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()

    return data