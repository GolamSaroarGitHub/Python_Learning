

import json
import requests
import pprint

accessToken= 'dGVzdHJlYWNodWl8aW5mb0B0ZXN0cmVhY2guYdfgdsf29tOjE1MTE0NjM2NTkyNjI6MDU0NDYwNzA2N2U4NzBhNTY4Nzg5ZmNmODg0ZjJjZDk'
url = 'https://testreachui.qtestnet.com/api/v3/projects/32348/test-cycles/278131'

headers = {'Content-type': 'application/json',
           'Authorization': 'dGVzdHJlYWNodWl8aW5mb0B0ZXN0cmVhY2guY29sdgtOjE1MTE0NjM2NTksdfI6MDU0NDYwNzA2N2U4NzBhNTY4Nzg5ZmNmODg0ZjJjZDk'
           }

response = requests.get(url, headers=headers)
pprint.pprint(response.json())

