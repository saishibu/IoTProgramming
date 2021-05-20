#NOTE: This program works for python2. Not tested for python3
#You can test it on python3. Suppose if there is any error especially with urllib, try running with python2

from flask import Flask
import pymysql

#Library to access external APIs (NOTE: This may not work with python3)
from urllib.request import urlopen

#For Python3 only
import requests


#Read OpenWeatherMap API usage here - https://openweathermap.org/api/one-call-api

#Insert your OpenWeatherMap API here
OPEN_WEATHER_MAP_API_KEY = "95c24917f8cc445dad4ea6113a933807"

app = Flask(__name__)
@app.route('/fetchWeather')
def get_open_weather_map_data():
  #give your Lattitude and Longitude
  lat = '8.01'
  lon = '77.05'
  
  #Create openweathermap url
  api_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&exclude=hourly,daily,currently,alerts+&appid="+OPEN_WEATHER_MAP_API_KEY+"&units=metric"
  print(api_url)
  #For Python2
  #response = urlopen(api_url).read()
  
  #For Python3
  response = requests.get(api_url).json()
  print(response)
  return response
# conn = mysql.connect()
# cur=conn.cursor()


if __name__ == "__main__":
  #Application runs on port 3000
  app.run(host="0.0.0.0", port='3000', debug=1)
