import json
import requests
import pprint

accessToken= 'dGVzdHJlYWNodWl8aW5mb0B0ZXN0cmVhY2guY29tOjE1MTE0NjM2NTkyNjI6MDU0NDYwNzA2N2U4NzBhNTY4Nzg5ZmNmODg0ZjJjZDk'
url = 'https://testreachui.qtestnet.com/api/v3/projects/32348/test-cases/5305779'



headers = {'Content-type': 'application/json',
           'Authorization': 'dGVzdHJlYWNodWl8aW5mb0B0ZXN0cmVhY2guY29tOjE1MTE0NjM2NTkyNjI6MDU0NDYwNzA2N2U4NzBhNTY4Nzg5ZmNmODg0ZjJjZDk'
           }




responses = requests.get(url, headers=headers)

# for response in responses:
pprint.pprint(responses.json())
# pp=responses.json()
# print(pp[0]['name'])
