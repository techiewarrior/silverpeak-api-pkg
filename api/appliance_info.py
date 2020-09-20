"""
************************************************************
This module is the API call to Orchestrator, which retrieves
information on each appliance.
************************************************************
"""

import json
import requests
from api_methods import ApiMethods

site_info = []

class ApplianceInfo:
    """ This class takes the list of dictionaries returned from the
        appliance info api call, and creates an object for each site.
        It also copies the attributes from the OrchHelper object created
        at the beginning to create the API session.  Each object is then
        added to the list 'site_list', so they can be iterated over and
        their attributes can be used for other functions. """

    def __init__(self, obj, entry):
        self.url = obj.url
        self.user = obj.user
        self.login_pwd = obj.password
        self.url_prefix = obj.url_prefix
        self.session = requests.Session()
        self.headers = obj.headers
        self.apiSrcId = "?source=menu_rest_apis_id"  # for API calls w/ just source as query param
        self.apiSrcId2 = "&source=menu_rest_apis_id"  # for API calls w/ multiple query params
        self.supportedAuthModes = ["local", "radius",
                                   "tacacs"]  # remote authentication modes supported via this helper module
        self.authMode = "local"  # change this to the desired auth mode before invoking login() function.
        self.id = entry["id"]
        self.uuid = entry["uuid"]
        self.networkRole = entry["networkRole"]
        self.site = entry["site"]
        self.sitePriority = entry["sitePriority"]
        self.username = entry["userName"]
        self.password = entry["password"]
        self.groupId = ["groupId"]
        self.IP = entry["IP"]
        self.webProtocolType = entry["webProtocolType"]
        self.serial = ["serial"]
        self.hasUnsavedChanges = entry["hasUnsavedChanges"]
        self.rebootRequired = entry["rebootRequired"]
        self.model = entry["model"]
        self.hardwareRevision = entry["hardwareRevision"]
        self.hostName = entry["hostName"]
        self.applianceId = entry["applianceId"]
        self.platform = entry["platform"]
        self.mode = entry["mode"]
        self.bypass = entry["bypass"]
        self.softwareVersion = entry["softwareVersion"]
        self.startupTime = entry["startupTime"]
        self.webProtocol = entry["webProtocol"]
        self.systemBandwidth = entry["systemBandwidth"]
        self.state = entry["state"]
        self.dynamicUuid = entry["dynamicUuid"]
        self.portalObjectId = entry["portalObjectId"]
        self.discoveredFrom = entry["discoveredFrom"]
        self.reachabilityChannel = entry["reachabilityChannel"]
        self.haPeer = entry["haPeer"]
        self.zoneList = entry["zoneList"]
        self.interfaceList = entry["interfaceList"]
        self.ip = entry["ip"]
        self.nePK = entry["nePk"]

    @classmethod
    def get_appliances(cls, obj):
        """ This method takes the OrchHelper object, which is passed
            to it, and passes both the object and appropriate url for the api
            call, to the 'GET' method in apicalls.py """

        r = ApiMethods.get("/appliance", obj)
        if r.status_code == 200:
            dict = r.json()
            for entry in dict:
                site_info.append(ApplianceInfo(obj, entry))
            return site_info
        else:
            print("{0}: unable to get appliance list: {1}".format(obj.url, r.text))
            return []

# end
