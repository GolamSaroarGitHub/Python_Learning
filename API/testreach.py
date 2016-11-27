# import requests
#
# from pprint import pprint
# city=input("Enter a city name for the corrent Temarature\n")
# def main():
#     response=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=8e96b8a4dca2cf1ed4d9d2d25842e568")
#     weather=response.json()
#     kel=weather['main']['temp']
#     cel=kel*0.0869
#     print("%.2f"%cel)
#     #
#     # for k,v in weather.items():
#     #     print(k)
#
#
# if __name__ == '__main__':
#     main()











import json
import requests
import pprint
url = 'https://cert.testreach.com/api/get_token'
data = {"app_id":"testreach1460718431715154199a6de3","secret":"13abb85fa5e67808ed0607fe4512e9a04b3019db"}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)
pprint.pprint(response.json())





