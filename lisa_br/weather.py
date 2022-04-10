
# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

#########################################################
#  LISA Weather API (LWA)
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
##########################################################

import os
import sys
try:
    import pyttsx3
    import argparse
    import pyowm
    from pyowm.utils.config import get_default_config
    import geopy
except ModuleNotFoundError:
    try:
        from leds import GradLed
        GradLed.error_msg_led()
        save('weather_man.py, line 12, ', 'error_log.txt', title = 'Errors In The Lisa Code:', w_t = True)    
    except:
        pass


# Variables
search = []
usr_choice=''
def get_usr_choice(usr_choice):
    usr_choice = usr_choice
try:
    config_dict = get_default_config()
    config_dict['language'] = 'pt'
    owm = pyowm.OWM('bd5f8357434bcf5aade2eb3a5487b84f', config_dict)
    mgr = owm.weather_manager()
except Exception as e:
    from lisa import save
    save('resweather.py, line 15 - 16, ' + str(e), 'error_log.txt', title = 'Errors In The Lisa Code:', w_t = True)

# Functions
def icestorm_results(query = ''):
    """Fastest results possible. More bugs than ever."""
    if query == "":
        query="aqui"
    if 'temperatura' in query:
        query=query.replace('temperatura', '')
        query = query.lstrip()
    import requests
    from bs4 import BeautifulSoup
    query = query.replace('+', '%2B')
    query = query.replace(' ', '+') # Replaces the spaces with '+' so that it becomes a undestandable link for google
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get('https://www.google.com/search?q=' + "temperatura " + str(query), headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    ID = ['wob_loc', 'cwos', 'tw-target-text', 'tw-target-text-container', 'kAz1tf', ''] # Answer ID is 'NotFQb'
    location = soup.find('div', class_='wob_loc q8U8x', id='wob_loc') #OLD: wob_loc mfMhoc
    if query != 'aqui':
        day = query.replace('+', '%2B')
        day = day.replace('%2B', ' ')
        day = day.replace('+', ' ')
    else:
        day='hoje'
    temperature = soup.find('span', class_='wob_t q8U8x', id='wob_tm') #OLD: wob_t TVtOme
    description = soup.find('div', class_='wob_dcp')
    precipitation = soup.find('span', id='wob_pp')
    humidity = soup.find('span', id='wob_hm')
    wind = soup.find('span', id='wob_ws') # OLD: wob_ws
    forecast_time = soup.find('span', class_='wob_dts')
    try:
        forecast_timm_flag_did_work = True
        forecast_time = forecast_time.text
    except:
        forecast_timm_flag_did_work = False
        forecast_time = day
    location = location.text
    temperature = temperature.text
    description = description.text
    precipitation = precipitation.text
    humidity = humidity.text
    wind = wind.text
    weather = {"location" : location,
               "day" : day,
               "temperature" : temperature, 
               "precipitation" : precipitation, 
               "humidity" : humidity,
               "wind" : wind,
               "description" : description,
               "forecast_time" : forecast_time,
               "forecast_time_did_work": forecast_timm_flag_did_work}
    return weather

def get_location(city = ''):
    try:
        if city == "":
            from geopy.geocoders import Nominatim 
            import geocoder
            geolocator = Nominatim(user_agent="current_weather")
            g = geocoder.ip('me')
            latlong = g.latlng
            latitude = latlong[0]
            longitude = latlong[1]
            location = geolocator.reverse(str(latitude) + "," + str(longitude)) 
            address = location.raw['address'] 
            loc=str(address['suburb']) + ", " + str(address['postcode']) + ", " + str(address['city'])
            return loc
        else:
            return city
    except:
        return 'Local não disponível'

def get_place_google(query = ''):
    if query == "":
        query="aqui"
    import requests
    from bs4 import BeautifulSoup
    query = query.replace('+', '%2B')
    query = query.replace(' ', '+') # Replaces the spaces with '+' so that it becomes a undestandable link for google
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get('https://www.google.com/search?q=' + "temperatura " + query, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    ID = ['wob_loc', 'cwos', 'tw-target-text', 'tw-target-text-container', 'kAz1tf', ''] # Answer ID is 'NotFQb'
    typ = ['div', 'span', 'td']
    #classes=['vk_bk TylWce', 'wob_t TVtOme']
    classes = ['wob_loc mfMhoc']
    for cl in classes:
        for t in typ:
            result = soup.find(t, class_=cl)
            if result == None:
                for i in ID:
                    result = soup.find(t, class_=cl, id=i)
                    if result != None:
                        return result.text
                return "Não disponível"
            else:
                return result.text
                break

def get_weather_description_google(query = ''):
    if query == "":
        query="temperatura aqui"
    import requests
    from bs4 import BeautifulSoup
    query = query.replace('+', '%2B')
    query = query.replace(' ', '+') # Replaces the spaces with '+' so that it becomes a undestandable link for google
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get('https://www.google.com/search?q=' + "temperatura em " + query, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    ID = ['cwos', 'tw-target-text', 'tw-target-text-container', 'kAz1tf', ''] # Answer ID is 'NotFQb'
    typ = ['div', 'span', 'td']
    #classes=['vk_bk TylWce', 'wob_t TVtOme']
    classes = ['wob_dcp']
    for cl in classes:
        for t in typ:
            result = soup.find(t, class_=cl)
            if result == None:
                for i in ID:
                    result = soup.find(t, class_=cl, id=i)
                return "Não disponível"
            else:
                return result.text
                break

def get_hpw_google(query = ''):
    if query == "":
        query="temperatura aqui"
    import requests
    from bs4 import BeautifulSoup
    query = query.replace('+', '%2B')
    query = query.replace(' ', '+') # Replaces the spaces with '+' so that it becomes a undestandable link for google
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get('https://www.google.com/search?q=' + "temperatura em " + query, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    precipitation = soup.find('span', id='wob_pp')
    precipitation = precipitation.text
    humidity = soup.find('span', id='wob_hm')
    humidity = humidity.text
    wind = soup.find('span', id='wob_ws')
    wind = wind.text
    hpw={"precipitation" : precipitation, "humidity" : humidity, "wind" : wind}
    return hpw

def get_temperature_google(query = ''):
    from search_at_google import get_google_result
    if query == "":
        return get_google_result("temperatura aqui")
    else:
        return get_google_result("temperatura em " + query)

def weather_temp(city: str):
    obs = mgr.weather_at_place(city)
    w = obs.weather
    return str(round(w.temperature('celsius')['temp']))

def weather_det(city: str):
    obs = mgr.weather_at_place(city)
    wea = obs.weather
    return str(wea.detailed_status)

def get_forecast_google(query = ''):
    if query == "":
        query = "temperatura amanhã"
        when = "amanhã"
    if "temperatura" not in query:
        query = "temperatura " + query
    from search_at_google import get_google_result
    import requests
    from bs4 import BeautifulSoup
    query = query.replace('+', '%2B')
    query = query.replace(' ', '+') # Replaces the spaces with '+' so that it becomes a undestandable link for google
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get('https://www.google.com/search?q=' + query, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    ntemp = str(get_google_result(query))
    npre = str(get_hpw_google(query)['precipitation'])
    nhum = str(get_hpw_google(query)['humidity'])
    nwind = str(get_hpw_google(query)['wind'])
    ndesc = str(get_weather_description_google(query))
    if query != "":
        when = soup.find('div', class_='QrNVmd Z1VzSb')
    forecast = {"temperature" : ntemp, "precipitation" : npre, "humidity" : nhum, "wind" : nwind, "description" : ndesc, "when" : when}
    return forecast

def get_weather_google(query):
    weather = {"temperature" : get_temperature_google(query), 
               "precipitation" : get_hpw_google(query)['precipitation'], 
               "humidity" : get_hpw_google(query)['humidity'],
               "wind" : get_hpw_google(query)['wind'],
               "description" : get_weather_description_google(query),
               "place" : get_place_google(query)}   
    return weather 

def get_weather_pyowm(query=get_location(usr_choice)):
    weather = {"temperature" : weather_temp(query),
               "description" : weather_det(query),
               "place" : query}
    return weather

# Pyowm weather info using local IP Adress (not that much precise):
#weather_info_a = str("A temperatura em " + str(get_location(usr_choice)) + " está por volta dos " + weather_temp(get_location(usr_choice)) + " graus celcius com " + weather_det(get_location(usr_choice)) + ".")