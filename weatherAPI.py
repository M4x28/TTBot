import requests
import emoji
from geopy.geocoders import Nominatim

# Emoji
switcher = {
    "Clear": " :sunrise:",
    "Rain": " :cloud_with_rain:",
    "Clouds": " :cloud:",
    "Snow": " :cloud_with_snow:",
    }

def kelvinCelsius(kelvin):
  kelvin -= float(273.15)
  celsius = str(round(kelvin)) + "°"
  return str(celsius)

def switchDate(date):
  vet = date.split('-')
  temp = vet[2]
  vet[2] = vet[0]
  vet[0] = temp
  result = vet[0] + '/' + vet[1] + '/' + vet[2]
  return result

def getWeather(location):
  
  url = "https://community-open-weather-map.p.rapidapi.com/forecast"

  querystring = {"q":location}

  headers = {
      'x-rapidapi-key': "44dc16f7ffmshdf7edb3ac5c2990p189d22jsn99d4beac9cdc",
      'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

  # Get data and convert it in json format 
  json_data = requests.request("GET", url, headers=headers, params=querystring).json()
  
  # Filter
  result = ''
  i = 0
  while i < 40:
    result += switchDate(json_data['list'][i]['dt_txt'][:10]) + ': ' + json_data['list'][i]['weather'][0]['description'].upper() + ', ' + kelvinCelsius(float(json_data['list'][i]['main']['temp'])) + emoji.emojize(switcher.get(json_data['list'][i]['weather'][0]['main'])) + '\n'

    i += 8

  return result


def getWeatherfromLocation(latitude, longitude):
  # initialize Nominatim API
  geolocator = Nominatim(user_agent="geoapiExercises")

  location = geolocator.reverse(str(latitude) + ',' + str(longitude))
  
  address = location.raw['address']
  
  # traverse the data
  city = address.get('city', '')
  code = address.get('country_code')
  position = city + ',' + code

  return getWeather(position)