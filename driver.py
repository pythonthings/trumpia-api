from trumpia_Utility import Trumpia
import time

def subscriptions(mobile_number,first_name,last_name):
    body = {
        'list_name':'ContactsList',
        'subscriptions':[
            {
                "first_name": first_name,
                "last_name": last_name,
                "mobile":
                {
                    "number":mobile_number,
                    "country_code":"1"
                },
                "voice_device": "mobile"
            }
        ]
    }
    subscription_status = obj.getSearchSubscription(mobile_number)
    if 'MPSE2305' in subscription_status :
        print("PUT SUB")
        request_id = obj.putSubscription(body)
        time.sleep(2)
        subscription_id = obj.getStatusReport(request_id)
    elif 'subscription_id_list' in subscription_status:
        print("POST SUB: ")
        subscription_id = subscription_status['subscription_id_list']
        subscription_id = str(subscription_id).strip("['']")
        subscription_data = obj.getSubscription(subscription_id)
        current_mobile_number = subscription_data['mobile']['value']
        if current_mobile_number != mobile_number:
            body = {
                'list_name':'ContactsList',
                'subscriptions':[
                    {
                        "mobile":
                        {
                            "number":mobile_number,
                            "country_code":"1"
                        },
                        "voice_device": "mobile"
                    }
                ]
            }
            request_id = obj.postSubscription(subscription_id,body)
            subscription_id = obj.getStatusReport(request_id)

        current_list_ids = subscription_data['list_ids']
        if 'first_name' in subscription_data:
            current_first_name = subscription_data['first_name']
            if current_first_name == first_name:
                pass
            else:
                body = {
                    'list_name':'ContactsList',
                    'subscriptions':[
                        {
                            "first_name": first_name,
                        }
                    ]
                }
                request_id = obj.postSubscription(subscription_id,body)
                subscription_id = obj.getStatusReport(request_id)
        if 'last_name' in subscription_data:
            current_last_name = subscription_data['last_name']
            if current_first_name == first_name:
                pass
            else:
                body = {
                    'list_name':'ContactsList',
                    'subscriptions':[
                        {
                            "last_name": last_name,
                        }
                    ]
                }
                request_id = obj.postSubscription(subscription_id,body)
                subscription_id = obj.getStatusReport(request_id)
        if 'last_name' not in subscription_data:
            body = {
                'list_name':'ContactsList',
                'subscriptions':[
                    {
                        "last_name": last_name,
                    }
                ]
            }
            request_id = obj.postSubscription(subscription_id,body)
            subscription_id = obj.getStatusReport(request_id)
    else:
        print(subscription_status)

def main():
    mobile_number = ''
    last_name = ''
    first_name = ''
    subscriptions(mobile_number,first_name,last_name)

if __name__ == '__main__':
    obj = Trumpia()
    main()
