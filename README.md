# mark-monitor<br>
> Purpose is to export list of domains from Mark Monitor<br>
<br>
Purpose of script is to export domains from Mark Monitor<br>
<br>
You can see the documentation for their REST API.  Note, I find that the documentation is only viewable on Firefox and Chrome.  It doesn't work with Safari for my system.

[Mark Monitor REST API Swagger](https://domains.markmonitor.com/domains/setup/restapi/)

<br>This script exports active domains.  You can adjust the results by modifying the "fields" variable.<br>
<br>
If your company requires two factor authentication, you can ask your Mark Monitor account rep to create a read-only API user account that won't require 2FA.<br>
<br>
I suggest that you use a read-only API user as a best practice.<br>
<br>

## Installation & Dependencies

Python 3.6 installed<br>
<br>
The following modules installed:<br>
1.  getpass<br>
2.  json<br>
3.  requests<br>
<br>

## Usage example

To run this from command line:<br>
<br>
```sh
./get-mark_monitor-data.py
```
<br>

The script performs these 4 things:<br>
1.  Creates a session
2.  Login with username/password and get a cookie
3.  Search for all domains with specific status
4.  Log out

These are configurable items in the script:
<br>
<b>Proxy Information:</b><br>
<br>
<br>
The script assumes you don't need to go through a proxy.  If you have a proxy setup at work, then edit the variables section of the script and put in the correct proxy for <i>http_proxy</i> & <i>https_proxy</i>.<br>
<br>
You will also need to change three lines of the script from:<br>
```sh
verify=False
```
to<br>
```sh
proxies=proxyDict, verify=False
```

<br>
<b>Search data used:</b><br>
<br>
<br>
The script adds the domain to the output file if the value is one of these:<br>
<br>
1.  abandoned<br>
2.  registered locked<br>
3.  registered unlocked<br>
4.  registrar hold<br>
5.  registered premium locked<br>
6.  registered super locked<br><br>

To view the complete list of possible domain statuses, look at [Mark Monitor Domain Statuses](https://domains.markmonitor.com/domains/setup/restapi/#!/Domain/findDomainById)



## Release History

* 0.0.1
    * Initial version

## Meta

Brian Bullard – [@BrianBullard94](https://twitter.com/BrianBullard94) – dns.dhcp.ipam@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/ddiguy/mark-monitor](https://github.com/ddiguy)

## Contributing

1. Fork it (<https://github.com/ddiguy/mark-monitor/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
