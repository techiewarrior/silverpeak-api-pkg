def OrchLogin(orchIP, user, password):
#
# Disable ssl inspection
    requests.packages.urllib3.disable_warnings()
#
# API call to login
    url = "https://{0}/gms/rest/authentication/login".format(orchIP)
    payload = "{{\r\n  \"user\": \"{0}\",\r\n  \"password\": \"{1}\",\r\n  \"token\": \"\",\r\n  \"loginType\": 0\r\n}}".format(user, password)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    orchCookie = response.cookies
#
# Print "response" and return "orchCookie" to main.py
    print(response)
    return(orchCookie)