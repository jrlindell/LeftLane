import json
import requests

# returns average visit duration
def avg_visit_dur(api_key, domain_name, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd):
    '''
    Output: Average visit duration for domain name for a country
    input:
        api_key = api_key for similarweb
        domain_name = url of company you want to see (ex. bbc.com)
        start_date = can go to 36 months
        end_date = can go back 36 months
        country = two letter country, all lowercase (ex. us, gb)
        main_domain_only = returns values for the main domain only if set to true
        granularity = daily, weekly, or monthly
        show_verified = show shared google analytics data if available
        mtd = When 'true', end_date is set to the latest available days' data (month-to-date). 
            To use, set granularity to 'daily'. mtd=true will charge 1 additional hit (2 hits total). Default value is 'false'
    '''

    url = "https://api.similarweb.com/v1/website/" + domain_name + "/total-traffic-and-engagement/average-visit-duration?api_key=" + api_key + \
        "&start_date=" + start_date + "&end_date=" + end_date + "&country=" + country + "&granularity=" + granularity + "&main_domain_only=" + \
            main_domain_only + "&format=json" + "&show_verified=" + show_verified + "&mtd=" + mtd
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    return data

# returns estimated number of visits for the domain
def pages_per_visit(api_key, domain_name, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd):
    '''
    Output: Average page views per visit for the given domain
    input:
        api_key = api_key for similarweb
        domain_name = url of company you want to see (ex. bbc.com)
        start_date = can go to 36 months
        end_date = can go back 36 months
        country = two letter country, all lowercase (ex. us, gb)
        main_domain_only = returns values for the main domain only if set to true
        granularity = daily, weekly, or monthly
        show_verified = show shared google analytics data if available
        mtd = When 'true', end_date is set to the latest available days' data (month-to-date). 
            To use, set granularity to 'daily'. mtd=true will charge 1 additional hit (2 hits total). Default value is 'false'
    '''
    url = "https://api.similarweb.com/v1/website/" + domain_name + "/total-traffic-and-engagement/pages-per-visit?api_key=" + api_key + \
        "&start_date=" + start_date + "&end_date=" + end_date + "&country=" + country + "&granularity=" + granularity + "&main_domain_only=" + \
            main_domain_only + "&format=json" + "&show_verified=" + show_verified + "&mtd=" + mtd
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    return data

# returns average page views per visit for the domain
def visits(api_key, domain_name, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd):
    '''
    Output: Estimated number of visits for the domain
    input:
        api_key = api_key for similarweb
        domain_name = url of company you want to see (ex. bbc.com)
        start_date = can go to 36 months
        end_date = can go back 36 months
        country = two letter country, all lowercase (ex. us, gb)
        main_domain_only = returns values for the main domain only if set to true
        granularity = daily, weekly, or monthly
        show_verified = show shared google analytics data if available
        mtd = When 'true', end_date is set to the latest available days' data (month-to-date). 
            To use, set granularity to 'daily'. mtd=true will charge 1 additional hit (2 hits total). Default value is 'false'
    '''
    url = "https://api.similarweb.com/v1/website/" + domain_name + "/total-traffic-and-engagement/visits?api_key=" + api_key + \
        "&start_date=" + start_date + "&end_date=" + end_date + "&country=" + country + "&granularity=" + granularity + "&main_domain_only=" + \
            main_domain_only + "&format=json" + "&show_verified=" + show_verified + "&mtd=" + mtd
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    return data