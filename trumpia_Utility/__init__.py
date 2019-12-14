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
                if 'status_code' in json_response:
                    status_code = json_response['status_code']
                    print('trumpia_Utility | Status code: {}'.format(status_code))
                    subscription_status = self.subscriptionStatusCodes(status_code)
                    print('trumpia_Utility | {}'.format(status_code + ': ' + subscription_status))
                    resp = str(status_code) + ': ' +str(subscription_status)
                    return resp
                elif 'subscription_id_list' in json_response:
                    print('trumpia_Utility | {}'.format(json_response))
                    return json_response
                else:
                    pass

            else:
                retry+=1
                print('Retry: {}'.format(retry))


    def getSubscription(self,subscription_id):
        retry = 0
        if len(subscription_id) <= 0:
            print(subscription_id)
            return
        while retry < 3:
            try:
                response = requests.request(METHOD[2],TRMURL + FUNCTION[0]+'/'+subscription_id,headers = HEADER)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print('trumpia_Utility | Error: {}'.format(str(err)))
            except requests.exceptions.Timeout as err_time:
                print('trumpia_Utility | Error: {}'.format(str(err_time)))

            if response.status_code == 200:
                json_response = response.json()
                print(json_response)
                print('trumpia_Utility GET SUB BY ID| json_response: {}'.format(json_response))
                return json_response
            else:
                retry+=1
                print('trumpia_Utility | Retry: {}'.format(retry))


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
                print('trumpia_Utility | Error: {}'.format(str(err)))
            except requests.exceptions.Timeout as err_time:
                print('trumpia_Utility | Error: {}'.format(str(err_time)))

            if response.status_code == 200:
                json_response = response.json()
                print(json_response)
                request_id = json_response['request_id']
                print('trumpia_Utility | Request id: {}'.format(request_id))
                return request_id
            else:
                retry+=1
                print('trumpia_Utility | Retry: {}'.format(retry))

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
                print('trumpia_Utility | Error: {}'.format(str(err)))
            except requests.exceptions.Timeout as err_time:
                print('trumpia_Utility | Error: {}'.format(str(err_time)))

            if response.status_code == 200:
                json_response = response.json()
                print(json_response)
                request_id = json_response['request_id']
                print('trumpia_Utility | Request id: {}'.format(request_id))
                return request_id
            else:
                retry+=1
                print('trumpia_Utility | Retry: {}'.format(retry))

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
                print('trumpia_Utility | Error: {}'.format(str(err)))
            except requests.exceptions.Timeout as err_time:
                print('trumpia_Utility | Error: {}'.format(str(err_time)))

            if response.status_code == 200:
                json_response = response.json()
                if 'status_code' in json_response:
                    status_code = json_response['status_code']
                    print('trumpia_Utility | Status code: {}'.format(status_code))
                    subscription_status = self.subscriptionStatusCodes(status_code)
                    print(status_code + ': ' + subscription_status)
                    return
                if 'subscription_id' in json_response:
                    subscription_id = json_response['subscription_id']
                    print('trumpia_Utility |POST SUBSCRIPTION ID:  {}'.format(subscription_id))
                    return subscription_id

                for data in json_response:
                    #FAILED PUT SUBSCRIPTION
                    if 'status_code' in data:
                        status_code = data['status_code']
                        print('trumpia_Utility |Status code: {}'.format(status_code))
                        subscription_status = self.subscriptionStatusCodes(status_code)
                        print(status_code + ': ' + subscription_status)
                    #SUCESSFUL PUT SUBSCRIPTION
                    if 'subscription_id' in data:
                        subscription_id = data['subscription_id']
                        print('SUCCESS PUT SUBSCRIPTION ID:  {}'.format(subscription_id))
                        return subscription_id
                break
            else:
                retry+=1
                print('Retry: {}'.format(retry))

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
