import json
import requests
import operator


# this is to show how i built this, but delete when trying to use and fill in the variables below
with open('data_examples/pages_per_visit.json', 'r') as f: # companies
    ppv = json.load(f)
with open('data_examples/avg_visit_dur.json', 'r') as f: # total_traffic
    avg_visit_duration = json.load(f)
with open('data_examples/top_sites_desktop.json', 'r') as f: # total_traffic
    desktop = json.load(f)


api_key = ''
industry = ''
country = ''
start_date = ''
end_date = ''
main_domain_only = ''
granularity = ''
show_verified = ''
mtd = ''
get_all = ''

# STEP 1: get all of the companies we could look at
from data import industry_analysis

top_mobile_sites = industry_analysis.top_sites_mobile(api_key, industry, start_date, end_date, country, get_all)
top_mobile_apps = top_mobile_sites['top_sites']
top_desktop_sites = industry_analysis.top_sites_desktop(api_key, industry, start_date, end_date, country, get_all)
top_desktop_apps = top_desktop_sites['top_sites']

# lets do an aggregate score, but in order to take into account both, we are going to do a rank of 1 = 100 points, 2 = 9, etc., so if a company
# is on both at 1, they get 200 points

def rank_score(top_mobile_apps, top_desktop_apps):
    agg = {}

    for i in top_mobile_apps:
        if i['domain'] in agg.keys():
            agg[i['domain']] += (1 + len(top_mobile_apps) - i['rank'])
        else:
            agg[i['domain']] = (1 + len(top_mobile_apps) - i['rank'])
    for j in top_desktop_apps:
        if j['domain'] in agg.keys():
            agg[j['domain']] += (1 + len(top_desktop_apps) - j['rank'])
        else:
            agg[j['domain']] = (1 + len(top_desktop_apps) - j['rank'])
    return agg
# now we have all of the top apps for both desktop and mobile, and a good way to distinguish their rank


## NOW LETS GET THE TRAFFIC NUMBERS FOR THE TOP X AMOUNT OF COMPANIES
## put domain names in domains ex. domains = ['bbc.com', 'spotify.com']
from data import total_traffic
### avg_visits_dur
def get_avg_visits_dur(api_key, domains, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd):
    avg_visits_score = {}
    for i in domains:
        avg_visit_duration = total_traffic.avg_visit_dur(api_key, i, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd)
        name = avg_visit_duration['meta']['request']['domain']
        avg_visits_score[name] = sum([x['average_visit_duration'] for x in avg_visit_duration['average_visit_duration']])
    return avg_visits_score

### pages per visit
def pages(api_key, domains, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd):
    ppv_score = {}
    for i in domains:
        ppv = total_traffic.pages_per_visit(api_key, i, country, start_date, end_date, main_domain_only, granularity, show_verified, mtd)
        name = ppv['meta']['request']['domain']
        ppv_score[name] = sum([x['pages_per_visit'] for x in ppv['pages_per_visit']])
    return ppv_score


# run the functions for the top X amount of companies you want, or just input domain names into apps
app_scores = rank_score(top_mobile_apps, top_desktop_apps)
apps = list(app_scores.keys())
avg_dur = get_avg_visits_dur(api_key, apps, country=country, start_date=start_date, end_date=end_date, 
                            main_domain_only=main_domain_only, granularity=granularity, show_verified=show_verified, mtd=mtd)
pgs_per_visit = pages(api_key, apps, country=country, start_date=start_date, end_date=end_date, 
                            main_domain_only=main_domain_only, granularity=granularity, show_verified=show_verified, mtd=mtd)

agg_scores = []
for comp in apps:
    new_agg_score = {}
    new_agg_score[comp] = app_scores[comp] + avg_dur[comp] + pgs_per_visit[comp]


# this outputs the final score in descending order
new_agg_score = dict( sorted(new_agg_score.items(), key=operator.itemgetter(1),reverse=True))



# make an aggregate for these different scores