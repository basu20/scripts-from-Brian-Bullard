#!/usr/local/bin/python3.6
import time
from datetime import date
import datetime
import getpass
import json
import requests
import sys
from os.path import expanduser
# Ignoring SSL warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

"""
================================================================================
Purpose and usage
================================================================================
Written by Brian Bullard, https://github.com/ddiguy/

https://twitter.com/BrianBullard94

Purpose of script is to export domains from Mark Monitor

You can see the documentation for their REST API:
https://domains.markmonitor.com/domains/setup/restapi/

This script exports active domains.  You can adjust the results by modifying
the "fields" variable.

If your company requires two factor authentication, you can ask your
Mark Monitor account rep to create a read-only API user account that isn't
2 factor.

I suggest that you use a read-only API user as a best practice.

================================================================================
Variables
================================================================================
"""
# Date and time
today = datetime.date.today ()
tday = today.strftime ("%Y-%m-%d")

"""
Proxy settings
If you need to set a proxy, then change this line 3 times in this script:
    verify=False
to
    proxies=proxyDict, verify=False

You will also need to specify the proxy in these variables
"""
http_proxy = "http://proxy.example.com:8080"
https_proxy = "https://proxy.example.com:8080"
proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy
            }

# Login credentials
username = input('Enter your username: ')
password = getpass.getpass("Enter your Password:")
credentials = {"username": username, "password": password}

# Output file
file_dir = expanduser('~') + '/'
zone_list_mm = file_dir + tday + '_mark-monitor_zones.csv'


# Mark Monitor API URLs
mm_base_url = 'https://domains.markmonitor.com/domains/restapi/v2/'
mm_login = mm_base_url + 'login'
mm_search_domain = mm_base_url + 'domains/search'
mm_logout = mm_base_url + 'logout'

# Search data used
fields = {"visibleFields": ["domainName","status"],"filters": [{"field": "status","values": ["abandoned","registered locked","registered unlocked","registrar hold","registered premium locked","registered super locked"]}]}

"""
================================================================================
Getting domains from Mark Monitor
================================================================================
This is a 4 step process
"""

# 1)  Create a session 
try:
    s = requests.Session()
except Exception as e:
    print('Unable to create session - '+str(e))
    sys.exit()

# 2)  Login with username/password and get a cookie
try:
    r1 = s.post(mm_login, headers={'Accept':'application/json',
        'Content-Type':'application/json'},
        data=json.dumps(credentials),
        verify=False)
    my_cookie = (r1.headers['Set-Cookie'])
except Exception as e:
    print('Unable to login and get cookie - '+str(e))
    sys.exit()


# 3)  Search for all domains with specific status
try:
    r2 = s.post(mm_search_domain, headers={'Accept':'application/json',
        'Content-Type':'application/json', 'Cookie ':'''+my_cookie+'''},
        data=json.dumps(fields),
        verify=False)

    a = json.loads(r2.text)
    d = a['domainList']
    o1 = open (zone_list_mm,'a')
    for i in d:
        a2 = str(i['domainName'])
        #print (a2)
        o1.write(a2 + '\n')
except Exception as e:
    print('Unable to get zone list - '+str(e))
    sys.exit()

# 4)  Log out
try:
    s.get(mm_logout, headers={'Accept':'application/json', 
        'Content-Type':'application/json', 'Cookie ':'''+my_cookie+'''}, 
        verify=False)
except Exception as e:
    print('Unable to logout - '+str(e))
    sys.exit()

