#!/usr/bin/python3
import requests, json, time,os

PATH = os.getcwd()
USERNAME = ''
TRMURL = 'https://api.trumpia.com/rest/v1/'+USERNAME+'/'
APIKEY = ''
HEADER = {
    'Content-Type': 'application/json',
    'x-apikey': APIKEY
}
METHOD = ['PUT','POST','GET','DELETE']
FUNCTION = ['subscription','report']

class Trumpia:

    def __init__(self):
        pass

    def getSearchSubscription(self,mobile_number):
        retry = 0
        if len(mobile_number) <= 0:
            print(mobile_number)
            return
        while retry < 3:
            try:
                response = requests.request(METHOD[2],TRMURL + FUNCTION[0]+'/'+'search?search_type=2&search_data='+mobile_number,headers = HEADER)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print('Error: {}'.format(str(err)))
            except requests.exceptions.Timeout as err_time:
                print('Error: {}'.format(str(err_time)))

            if response.status_code == 200:
                json_response = response.json()
                subscription_id = json_response['subscription_id_list']
                print(str(subscription_id).strip('''['']'''))
                return str(subscription_id).strip('''['']''')
            else:
                retry+=1
                print('Retry: {}'.format(retry))

    def putSubscription(self,body):
        retry = 0
        if len(body) <= 0:
            print(body)
            return
        while retry < 3:
            try:
                response = requests.request(METHOD[0],TRMURL + FUNCTION[0],json = body,headers = HEADER)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print('Error: {}'.format(str(err)))
            except requests.exceptions.Timeout as err_time:
                print('Error: {}'.format(str(err_time)))

            if response.status_code == 200:
                json_response = response.json()
                print(json_response)
                request_id = json_response['request_id']
                print('Request id: {}'.format(request_id))
                return request_id
            else:
                retry+=1
                print('Retry: {}'.format(retry))

    def postSubscription(self,subscription_id,body):
        retry = 0
        if len(str(subscription_id)) <= 0 or len(body) <= 0:
            print(subscription_id)
            return
        while retry < 3:
            try:
                response = requests.request(METHOD[1],TRMURL + FUNCTION[0]+'/'+str(subscription_id),json = body,headers = HEADER)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print('Error: {}'.format(str(err)))
            except requests.exceptions.Timeout as err_time:
                print('Error: {}'.format(str(err_time)))

            if response.status_code == 200:
                json_response = response.json()
                print(json_response)
                request_id = json_response['request_id']
                print('Request id: {}'.format(request_id))
                return request_id
            else:
                retry+=1
                print('Retry: {}'.format(retry))

    def getStatusReport(self,request_id):
        retry = 0
        if len(request_id) <= 0:
            print(request_id)
            return
        while retry < 3:
            try:
                response = requests.request(METHOD[2],TRMURL + FUNCTION[1]+'/'+request_id,headers = HEADER)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print('Error: {}'.format(str(err)))
            except requests.exceptions.Timeout as err_time:
                print('Error: {}'.format(str(err_time)))

            if response.status_code == 200:
                json_response = response.json()
                for data in json_response:
                    print(data)
                    #FAILED PUT SUBSCRIPTION
                    if 'status_code' in data:
                        print('inside if')
                        print(data)
                        status_code = data['status_code']
                        print(status_code)
                        print('Status code: {}'.format(status_code))
                        subscription_status = self.subscriptionStatusCodes(status_code)
                        print(status_code + ': ' + subscription_status)
                    #SUCESSFUL PUT SUBSCRIPTION
                    if 'subscription_id' in data:
                        subscription_id = data['subscription_id']
                        print('SUCCESS PUT SUBSCRIPTION ID:  {}'.format(subscription_id))
                        return subscription_id
                    #FAILED POST SUBSCRIPTION (NEED TO FINISH)
                    # if 'status_code' in data:
                    #     status_code = data['status_code']
                    #     print('Status code: {}'.format(status_code))
                    #     subscription_status = self.subscriptionStatusCodes(status_code)
                    #     print(status_code + ': ' + subscription_status)
                    #SUCCESS POST SUBSCRIPTION NEED TO FINISH
                break
            else:
                retry+=1
                print('Retry: {}'.format(retry))


    """
    SUCCESS PUT Subscription
    [
        {
            "subscription_id": 525031205,
            "push_id": 1079700919,
            "request_id": "T19121018385192d77c6f"
        }
    ]

    FAIL PUT SUB response
    [
        {
            "status_code": "MPSE1106",
            "requested_data": {
                "voice_device": "mobile",
                "push_id": 1079633327,
                "mobile": {
                    "number": "714342749",
                    "country_code": "1"
                },
                "request_id": "T19121016180775a99160"
            }
        }
    ]

    SUCCESS POST SUB
    {
        "subscription_id": 525022199,
        "push_id": 1079700092,
        "message": "Success Update Subscription.",
        "request_id": "T1912101834466870fbf1"
    }

    FAIL POST SUB response
    {
    "status_code": "MPSE1202",
    "push_id": 1079707577,
    "request_id": "T1912101907588be8959c"
    }

    """

    def subscriptionStatusCodes(self,status_code):
        file = open(PATH+'/trumpia_Utility/subscriptionStatusCodes.txt','r')
        subscription_status_codes = {}
        for codes in file:
            key, value = codes.split('\t')
            subscription_status_codes[key] = value

        if status_code in subscription_status_codes:
            subscription_status = subscription_status_codes[status_code]
        else:
            print('Status code: {} not in subscriptionStatusCodes'.format(status_code))

        return subscription_status
