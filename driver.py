from trumpia_Utility import Trumpia
import time



"""
==================
FAIL POST SUB response
{
    "status_code": "MPSE1202",
    "push_id": 1079707577,
    "request_id": "T1912101907588be8959c"
}
==================
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

==============
SUCCESS POST SUB
{
    "subscription_id": 525022199,
    "push_id": 1079700092,
    "message": "Success Update Subscription.",
    "request_id": "T1912101834466870fbf1"
}

SUCCESS PUT Subscription
[
    {
        "subscription_id": 525031205,
        "push_id": 1079700919,
        "request_id": "T19121018385192d77c6f"
    }
]
"""

obj = Trumpia()
# body = {
#     'list_name':'ContactsList',
#     'subscriptions':[
#         {
#             "email":"@gmail.com",
#         }
#     ]
# }
# #obj.subscriptionStatusCodes()
# request_id = obj.putSubscription(body)
#
# subscription_id = obj.getStatusReport(request_id)
#
#
# body = {
#     'list_name':'ContactsList',
#     'subscriptions':[
#         {
#             "email":"",
#             "mobile":
#             {
#                 "number":"",
#                 "country_code":"1"
#             },
#             "voice_device": "mobile"
#
#         }
#     ]
# }
request_id = obj.postSubscription(subscription_id,body)
subscription_id = obj.getStatusReport(")
