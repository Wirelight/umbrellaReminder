#! python3
"""
umbrellaReminder.py - Texts a reminder to bring an umbrella if rain is forecast within the next 12 hours. 

Configure OpenWeatherMap, Twilio and Personal info in config.py
"""

import json, requests
import config as cfg
from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(cfg.ACCOUNTSID, cfg.AUTHTOKEN)
    twilioCli.messages.create(body=message, from_=cfg.TWILIONUMBER, to=cfg.CELLNUMBER)

def getWeather():
    url='https://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=4&appid=%s'\
    % (cfg.LOCATION,cfg.APPID)
    response=requests.get(url)
    response.raise_for_status()
    weatherData=json.loads(response.text)
    w=weatherData['list']
    print(w)
    return w

def checkForRain():
    w = getWeather()
    if (w[0]['weather'][0]['main'] or w[0]['weather'][1]['main'] \
    or w[0]['weather'][2]['main'] or w[0]['weather'][3]['main'])=='Rain':
        textmyself('Bring an umbrella, %s. Rain is due today!' % cfg.NAME)

checkForRain()