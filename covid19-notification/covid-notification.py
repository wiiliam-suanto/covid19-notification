#!/usr/bin/env python3

import json
import notify2
import requests
import time
from datetime import datetime

infoURL = "https://kawalcovid19.id/"
timeInterval = 60

try :
    requests.get('https://api.covid19api.com/')
    status = "Connected"
    connection = True
except :
    status = "Not connect"
    connection = False
print(status)

def initSystem():
    url = "https://api.covid19api.com/live/country/indonesia"
    response_data = requests.get(url).json()
    todayTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for element in response_data:
        country = element['Country']
        confirm = element['Confirmed']
        death = element['Deaths']
        recovered = element['Recovered']
        #lastUpdate = element['Date']
    
    stringList = ['Country : ',country, '\n', 
                  'Confirmed : ',confirm, '\n',
                  'Death : ',death, '\n',
                  'Recovered : ',recovered, '\n',
                  'Time : ', todayTime, '\n',
                  'Visit this site for more information : ', infoURL
                 ]
    stringOutput = ''.join(str(i) for i in stringList )

    notify2.init("Covid19 Notification")
    notification = notify2.Notification("Covid19 Notification", stringOutput, "emblem-information")
    notification.set_urgency(2)
    notification.show()
    
while True:
    notify2.uninit()
    initSystem()
    time.sleep(timeInterval*60)