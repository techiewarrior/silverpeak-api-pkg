Collection of functions for Silver Peak API calls,
contained in a package called 'api'.  When 'api' package
is imported, it imports all functions from each module
in the package.  To call a function from one of the modules,
preface the function with "api.".

For example, to pass login variables to the function 'OrchLogin'
in the 'login.py' module, use 'api.OrchLogin(orchIP, user, password)'.

Additional modules will be added, as the need arises.

v2.0.0-OOP
     - This branch is to convert the package to an OOP design.
     - base_main.py is the starting template
     - The following have already been converted to OOP:
         - __init__.py
         - api_methods.py
         - appliance_info.py
         - login.py
     - Need to convert:
         - preconfigOrch.py
         - spcustomFile.py
         - yamlConversion.py

