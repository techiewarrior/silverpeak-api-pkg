"""
***********************************************************************
This base script reuests general information on each appliance from 
the Orchestrator, and it returns the detail of each appliance
as a list of objects in the list 'site_list'.  It can be used as
the base script to build on, when performing calls to Orchestrator
and appliances.
***********************************************************************
"""

import api

# User input for needed variables
url = input("OrchIP: ")
user = input("UserId: ")
pwd = input("Password: ")

api_session = api.OrchHelper(url, user, pwd)  # Create OrchHelper object

# for MFA login:
#    api_session.send_mfa()
#    mfa = input("Enter MFA code: ")
#    api_session.mfa_login(mfa)

site_list = api_session.login()  # Call login method on OrchHelper object

# Add addtional code here

api_session.logout()


# end
