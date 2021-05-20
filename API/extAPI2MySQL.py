#NOTE: This program works for python2 & python3
#Suppose if there is any error, especially with urllib (uncomment), try running with python2

from flask import Flask
import pymysql

#Library to access external APIs (NOTE: This may not work with python3)
#from urllib.request import urlopen

#For Python3 only
import requests


#Read OpenWeatherMap API usage here - https://openweathermap.org/api/one-call-api

#Insert your OpenWeatherMap API here
OPEN_WEATHER_MAP_API_KEY = "95c24917f8cc445dad4ea6113a933807"

#give your Lattitude and Longitude
lat = '8.01'
lon = '77.05'

#Create openweathermap url
api_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&exclude=hourly,daily,minutely,alerts+&appid="+OPEN_WEATHER_MAP_API_KEY+"&units=metric"
 
app = Flask(__name__)
@app.route('/fetchWeather')
def get_open_weather_map_data():
  
  #For Python2
  #response = urlopen(api_url).read()
  
  #For Python3
  response = requests.get(api_url).json()
  
  print(response)
  return response

@app.route('/todb')
def todb():
 response = requests.get(api_url).json()
 currentWeather = response['current']
 weatherReport = currentWeather['weather']
 return weatherReport

# conn = mysql.connect()
# cur=conn.cursor()


if __name__ == "__main__":
  #Application runs on port 3000
  app.run(host="0.0.0.0", port='3000', debug=1)
