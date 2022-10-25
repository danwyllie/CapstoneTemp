from flask import Flask, request, render_template
import requests
import datetime
from os import environ 

API_KEY = environ.get('API_KEY')
print("\nAPI_KEY:")
print(API_KEY)

app = Flask(__name__)
  
@app.route('/', methods =["GET", "POST"])
def index(): 
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":       
        cityName = request.form.get("cityName")  
        if cityName:
            #weatherApiKey = '21e4c7371396d617e2c79a86021070c9'
            #url = "https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid="+weatherApiKey+"&units=metric"
            url = "https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid="+API_KEY+"&units=metric"
            r = requests.get(url).json()

            print("\nAPI response:")
            print(r['cod'])

            if r['cod']==(200):
                print("\nRunning API query against URL:")
                print(url)
                print("\nopenweathermap API output :")
                print(r)
                SunriseTime = datetime.datetime.fromtimestamp(r['sys']['sunrise'])
                SunsetTime = datetime.datetime.fromtimestamp(r['sys']['sunset'])
                ConvertedSunrise = f"{SunriseTime:%Y-%m-%d %H:%M:%S}"
                ConvertedSunset = f"{SunsetTime:%Y-%m-%d %H:%M:%S}"
                Temperature = round(r['main']['temp'])
                weatherData = {
                    'Name' : r['name'],
                    'CountryCode' : r['sys']['country'],
                    'CordsLon' : r['coord']['lon'],
                    'CordsLat' : r['coord']['lat'],
                    'Temp' : Temperature,
                    'Description' : r['weather'][0]['main'],
                    'Icon' : r['weather'][0]['icon'],
                    'Sunrise' : ConvertedSunrise,
                    'Sunset' : ConvertedSunset,
                }
                print("\nIsolated 'weatherData' being used:")
                print(weatherData)
            if r['cod']==(404):
                print("City not found!")
        else:
            print("City not found!!")
            error = 1
    else:
        print("City not found!!!")
    return render_template('index.html', data = weatherData, cityName = cityName, error = error)
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
