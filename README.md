# SilverPeak-functions
# git alias = 'sp-api-pkg'

Collection of functions for Silver Peak API calls,
contained in a package called 'api'.  When 'api' package
is imported, it imports all functions from each module
in the package.  To call a function from one of the modules,
preface the function with "api.".

For example, to pass login variables to the function 'OrchLogin'
in the 'login.py' module, use 'api.OrchLogin(orchIP, user, password)'.
