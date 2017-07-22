# mark-monitor<br>
> Purpose is to export list of domains from Mark Monitor<br>
<br>
Purpose of script is to export domains from Mark Monitor<br>
<br>
You can see the documentation for their REST API:<br>
[Mark Monitor REST API Swagger](https://domains.markmonitor.com/domains/setup/restapi/)<br>
<br>
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
<br>
## Usage example<br>
<br>
To run this from command line:<br>
<br>
```sh
./get-mark_monitor-data.py
```
<br>

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
