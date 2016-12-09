
import json
import requests
import pprint

accessToken= 'dGVzdHJlYWNodWl8aW5mb0B0ZXN0cmVhY2guY29tOjE1MTE0NjM2NTkyNjI6MDU0NDYwNzA2N2U4NzBhNTY4Nzg5ZmNmODg0ZjJjZDk'
url = 'https://testreachui.qtestnet.com/api/v3/projects/32348/defects/538666'

headers = {'Content-type': 'application/json',
           'Authorization': 'dGVzdHJlYWNodWl8aW5mb0B0ZXN0cmVhY2guY29tOjE1MTE0NjM2NTkyNjI6MDU0NDYwNzA2N2U4NzBhNTY4Nzg5ZmNmODg0ZjJjZDk'
           }


#        }
data={
"candidates": [
{
"candidate_id": "abcd1234_89",
"salutation": "",
"firstname": "John_89",
"lastname": "Doe_89",
"organization": "TestReach Ltd.",
"tags": [
'Oslo', 'DP'
],
"email": "xyz_89@mail.com",
"mobile_number": "+xxxxxxxxxx",
# // "rollup_admin": "", ‐ Field Deprecated
"send_email": 'false',
"role": "ROLE_CANDIDATE",
"exam_id": "03"
},
{
"candidate_id": "abcd1235_891",
"salutation": "",
"firstname": "John_891",
"lastname": "Doe_891",
"organization": "TestReach Ltd.",
"tags": [
'Oslo', 'DP',
],
"email": "zyx_891@gmail.com",
"mobile_number": "+xxxxxxxxx",
# //"rollup_admin": “” – Field deprecated
"send_email": 'true',
"role": "ROLE_CANDIDATE",
"exam_id": "01"
}
]
}



responses = requests.get(url, headers=headers)

# for response in responses:
pprint.pprint(responses.json())
# pp=responses.json()
# print(pp[0]['name'])
