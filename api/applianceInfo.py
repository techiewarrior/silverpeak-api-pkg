"""
********

This module retrieves information on all appliances.

********
"""

def applianceINFO(orchIP, loginCookie):

    import requests
    import json

# Surpress ssl certificate verifcation warnings

    requests.packages.urllib3.disable_warnings()

# Request for appliance info - all

    url = "https://{0}/gms/rest/appliance".format(orchIP)
    headers = {'Content-Type': 'application/json'}

    response = requests.request("GET", url, headers=headers, cookies=loginCookie, verify=False)

# Deserialize json from API call to 'json_response'

    json_response = json.loads(response.text)

    return json_response

#end
