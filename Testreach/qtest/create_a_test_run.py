# POST /api/v3/projects/{projectId}/test-runs?parentId=278131&parentType=release
#releaseId=278131


import requests
import pprint
import json


accessToken= 'dGVzdHJlYWNodWl8aW5mb0B0ZXN0cmVhY2guY29tOjE1MTE0NjM2NTkyNjI6MDU0NDYwNzA2N2U4NzBhNTY4Nzg5ZmNmODg0ZjJjZDk'
url = 'https://testreachui.qtestnet.com/api/v3/projects/32348/test-runs?parentId=121442&parentType=release'



headers = {'Content-type': 'application/json',
           'Authorization': 'dGVzdHJlYWNodWl8aW5mb0B0ZXN0cmVhY2guY29tOjE1MTE0NjM2NTkyNjI6MDU0NDYwNzA2N2U4NzBhNTY4Nzg5ZmNmODg0ZjJjZDk'
           }

data={

"test_case": {
"id": 5305779
                        # //optionally specify a test case version
},
"name": "TR023008"
}

data_json = json.dumps(data)


responses = requests.post(url,data=data_json, headers=headers)

# for response in responses:
pprint.pprint(responses.json())
# pp=responses.json()
# print(pp[0]['name'])
