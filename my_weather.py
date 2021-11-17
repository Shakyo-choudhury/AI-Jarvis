from my_inputs import talk, take_command
import requests

def api():
    api_key = "560da8aa46d3ec09a781846c66798a10"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    talk('please say me your city name')
    city_name = take_command()
    print(city_name)
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        temp_feel_like = main['feels_like']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_report = data['weather']
        wind_report = data['wind']
        talk('the weather is')
        talk(temperature)
        talk(temp_feel_like)
        talk(humidity)
        talk(pressure)
        talk(weather_report)
        talk(wind_report)
            
    else:
        talk('http error')
def weather_api():
    fgkto=1
    while fgkto<2:
        api()
        fgkto=fgkto+1
if __name__==("__main__"):
    api()
    weather_api()