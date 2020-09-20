"""
***************************************************************************
This module contains the API methods, for API calls.  OrchHelper object
gets passed to each API method, depending on the type of call - i.e.
'POST', 'GET', 'PUT', 'DELETE'.
***************************************************************************
"""

import requests

class ApiMethods:

    """ Methods for API calls """

    @classmethod
    def post(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        data = {"user": obj.user, "password": obj.password,
                "loginType": obj.supportedAuthModes.index(obj.authMode)}
        return obj.session.post(obj.url_prefix + url + apiSrcStr, json=data,
                                verify=False, timeout=120,
                                headers=obj.headers)

    @classmethod
    def get(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.get(obj.url_prefix + url + apiSrcStr, verify=False,
                               timeout=120, headers=obj.headers)

    @classmethod
    def delete(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.delete(obj.url_prefix + url + apiSrcStr,
                                  verify=False, timeout=120,
                                  headers=obj.headers)

    @classmethod
    def put(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.put(obj.url_prefix + url + apiSrcStr, json=data,
                               verify=False, timeout=120,
                                headers=obj.headers)

