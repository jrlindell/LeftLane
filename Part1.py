import json
import requests

with open('data_examples/avg_visit_dur.json', 'r') as f: # companies
    avg_visit_dur = json.load(f)
with open('data_examples/top_sites_desktop.json', 'r') as f: # total_traffic
    desktop = json.load(f)


api_key = ''
country = ''
start_date = ''
end_date = ''
main_domain_only = ''
granularity = ''
show_verified = ''
mtd = ''

# STEP 1: get all of the companies we could look at
from data import industry_analysis

top_mobile_sites = industry_analysis.top_sites_mobile(api_key, industry, start_date, end_date, country, get_all)
top_mobile_apps = top_mobile_sites['top_sites']
top_desktop_sites = industry_analysis.top_sites_desktop(api_key, industry, start_date, end_date, country, get_all)
top_desktop_apps = top_desktop_sites['top_sites']

# lets do an aggregate score, but in order to take into account both, we are going to do a rank of 1 = 100 points, 2 = 9, etc., so if a company
# is on both at 1, they get 200 points

def rank_score(top_mobile_sites, top_desktop_sites):
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
    return agg
# now we have all of the top apps for both desktop and mobile, and a good way to distinguish their rank


## NOW LETS GET THE TRAFFIC NUMBERS FOR THE TOP X AMOUNT OF COMPANIES
from data import total_traffic
### avg_visits_dur
def get_avg_visits_dur(api_key, domains, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd):
    data, scores = [], []
    for i in domains:
        dur = {}
        avg_visit_duration = total_traffic.avg_visit_dur(api_key, i, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd)
        name = avg_visit_duration['meta']['request']['domain']
        durs = avg_visit_duration['average_visit_duration']
        dur[name] = durs
        data.append(dur)
    for name in domains:
        for d in len(data[name]):
            dom_score = []
            if name in dom_score.keys():  
                dom_score[name] += data[name][d]['average_visit_duration']
            else:
                dom_score[name] = data[name][0]['average_visit_duration']
    return dom_score

    
### pages per visit
def pages(api_key, domains, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd):
    data, scores = [], []
    for i in domains:
        pg = {}
        ppv = total_traffic.pages_per_visit(api_key, i, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd)
        name = ppv['meta']['request']['domain']
        pgs = ppv['pages_per_visit']
        pg[name] = pgs
        data.append(pg)
    for name in domains:
        for d in len(data[name]):
            ppv_score = []
            if name in ppv_score.keys():  
                ppv_score[name] += data[name][d]['pages_per_visit']
            else:
                ppv_score[name] = data[name][0]['pages_per_visit']
    return ppv_score

app_scores = rank_score(top_mobile_apps, top_desktop_apps)
apps = app_scores.keys()
avg_dur = get_avg_visits_dur(api_key, apps, country=country, start_date=start_date, end_date=end_date, 
                            main_domain_only=main_domain_only, granularity=granularity, show_verified=show_verified, mtd=mtd)
pgs_per_visit = pages(api_key, apps, country=country, start_date=start_date, end_date=end_date, 
                            main_domain_only=main_domain_only, granularity=granularity, show_verified=show_verified, mtd=mtd)

agg_scores = []




# make an aggregate for these different scores