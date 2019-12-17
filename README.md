![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue)
![PyPI - Requests Version](https://img.shields.io/badge/requests-2.22-green)

# trumpia-api
Trumpia API class for subscription, lists, messaging, and status report
- PUT SUBSCRIPTION
- GET REPORT FOR PUT SUBSCRIPTION
- POST SUBSCRIPTION
- GET REPORT FOR POST SUBSCRIPTION
- GET SEARCH SUBSCRIPTION by mobile number
- GET SUBSCRIPTION BY SPECIFIC ID
- SMS FUNCTION - in progress

### Setup
- (Recommended) create your virtual environment
  - python3.7 -m venv env
    - source env/bin/activate
- install requests
  - python3.7 -m pip install requests

### Flow
- driver.py has two functions
    - main(): calls subscriptions
    - subscription(): adds new contacts/updates existing contacts (first and or last name only)

## API Documentation
 - [Trumpia REST API](http://classic.trumpia.com/api/docs/rest/overview.php)
 - [Trumpia Subscriptions](http://classic.trumpia.com/api/docs/rest/functions/subscription.php)
 - [Trumpia Lists](http://classic.trumpia.com/api/docs/rest/functions/list.php)
 - [Trumpia SMS Direct](http://classic.trumpia.com/api/docs/rest/functions/direct-sms.php)
 - [Trumpia Status Report](http://classic.trumpia.com/api/docs/rest/functions/report.php)
 - [Trumpia System Status Codes](http://classic.trumpia.com/api/docs/rest/status-code.php)
