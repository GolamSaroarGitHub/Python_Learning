

import json
import requests
import pprint

accessToken= 'b8fe7676dcbd49f3ff3a5cf744e21fdf2694aea0046c57461744445805de192d'
url = 'https://cert.testreach.com/api/post_candidates'
# data = {
#
# "candidate_id": "golam_saroar_1234",
# "firstname": "golam123",
# "lastname": "saroar123",
# "organization": "Testreach",
# "tags":"sitting for exam",
# "send_email": 'false',
# "role": "ROLE_CANDIDATE"
#
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


data_json = json.dumps(data)
print(data_json)
headers = {'Content-type': 'application/json','authorization': 'Bearer b8fe7676dcbd49f3ff3a5cf744e21fdf2694aea0046c57461744445805de192d'}
response = requests.post(url, data=data_json, headers=headers)
pprint.pprint(response.json())

