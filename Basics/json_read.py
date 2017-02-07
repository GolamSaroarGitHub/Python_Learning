import json
from pprint import pprint
from os.path import exists

with open('sample.json') as data_file:
    print(exists("sample.json"))
    data = json.load(data_file)


    if "Browser_Stack" in data.keys():
        print('Exists')
        print(data["Browser_Stack"][0]["url"])

    else:
        print('Not Exists')