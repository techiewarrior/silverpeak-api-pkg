def preconfigUpload(orchIP, loginCookie, name, tag, data):
# Upload preconfiguration via REST API
#
# Surpress ssl certificate verifcation warnings
    requests.packages.urllib3.disable_warnings()
#
    url = "https://{0}/gms/rest/gms/appliance/preconfiguration".format(orchIP)
    payload = "{{\r\n  \"name\": \"{0}\",\r\n  \"serialNum\": null,\r\n  \"tag\": \"{1}\",\r\n  \"comment\": null,\r\n  \"autoApply\": true,\r\n  \"configData\": \"{2}\"\r\n}}".format(name, tag, data)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload, cookies=loginCookie, verify=False)
    print(response.text.encode('utf8'))
#     
# end
