import json
import requests

with open('data_examples/avg_visit_dur.json', 'r') as f: # companies
    avg_visit_dur = json.load(f)
with open('data_examples/top_sites_desktop.json', 'r') as f: # total_traffic
    desktop = json.load(f)

# STEP 1: get all of the companies we could look at
from data import industry_analysis

top_mobile_sites = industry_analysis.top_sites_mobile(api_key, industry, start_date, end_date, country, get_all)
top_mobile_apps = top_mobile_sites['top_sites']
top_desktop_sites = industry_analysis.top_sites_desktop(api_key, industry, start_date, end_date, country, get_all)
top_desktop_apps = top_desktop_sites['top_sites']

# lets do an aggregate score, but in order to take into account both, we are going to do a rank of 1 = 100 points, 2 = 9, etc., so if a company
# is on both at 1, they get 200 points
agg = {}

for i in top_mobile_sites:
    if i['domain'] in agg.keys():
        agg[i['domain']] += (1 + len(top_mobile_sites) - i['rank'])
    else:
        agg[i['domain']] = (1 + len(top_mobile_sites) - i['rank'])
for j in top_desktop_sites:
    if j['domain'] in agg.keys():
        agg[j['domain']] += (1 + len(top_desktop_sites) - j['rank'])
    else:
        agg[j['domain']] = (1 + len(top_desktop_sites) - j['rank'])
# now we have all of the top apps for both desktop and mobile, and a good way to distinguish their rank


## NOW LETS GET THE TRAFFIC NUMBERS FOR THE TOP X AMOUNT OF COMPANIES
from data import total_traffic
### avg_visits_dur
def get_avg_visits_dur(api_key, domain_names, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd):
    data, scores = [], []
    for i in domain_names:
        dur = {}
        avg_visit_duration = total_traffic.avg_visit_dur(api_key, i, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd)
        name = avg_visit_duration['meta']['request']['domain']
        durs = avg_visit_duration['average_visit_duration']
        dur[name] = durs
        data.append(dur)
    for name in domain_name:
        for d in len(data[name]):
            dom_score = []
            if name in dom_score.keys():  
                dom_score[name] += data[name][d]['average_visit_duration']
            else:
                dom_score[name] = data[name][0]['average_visit_duration']
    return dom_score

    



### pages per visit



### visits



# STEP 2: get relevant data for those companies that may be of interest


# STEP 3: analyze that data to see what companies could be best


# STEP 4: compare them to our companies