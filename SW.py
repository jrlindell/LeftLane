# Using the SW API come up with a tool that will surface promising companies for Left Lane
# to reach out to as potential investment targets. You can select which attributes (visits, unique visitors,
# page views, category rank, etc.) are the characteristics you want to use as the model input.
# Using whatever tool you wish, design and create an API script that will pull down company websites
# that could make interesting investment targets for Left Lane.
# Left Lane can run the code / program on our end once the code is shared as we have the auth/secret
# on our end but are not allowed to share outside of our organization.

import requests

api_key = "549cbf8246c449308ff25bf77221ce14"

url = "https://api.similarweb.com/v1/website/bbc.com/total-traffic-and-engagement/visits?api_key=" + api_key + "&start_date=2017-11&end_date=2018-01&country=gb&granularity=monthly&main_domain_only=false&format=json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

z = 2


