import requests

from pprint import pprint
city=input("Enter a city name for the corrent Temarature\n")
def main():
    response=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=8e96b8a4dca2cf1ed4d9d2d25842e568&units=metric")
    weather=response.json()
    kel=weather['main']['temp']
    # cel=kel*0.0869
    print("%.2f"%kel)
    #
    # for k,v in weather.items():
    #     print(k)


if __name__ == '__main__':
    main()