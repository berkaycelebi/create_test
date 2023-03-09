import requests
import time
import threading
import random

url = "https://localhost:5001/"

def weatherForecastTest():
    body = {
        "date": "2019-04-01",
        "location": "Kolkata",
        "temperature": 30,
        "summary": "Sunny"
    }

    i = 0
    while (i < 1):
        myrandom = random.randint(0, 500)

        r = requests.post(url+"WeatherForecast/",
                          headers={"Content-Type": "application/json", },
                          json=body)

        time.sleep(0.01)
        print(r.text)

    r = requests.post(url+"/WeatherForecast/",
                      headers={"Content-Type": "application/json", },
                      json=body)

    print(r.status_code)
    
threads = []
for i in range(80):
    threads.append( threading.Thread(target=weatherForecastTest))

for thread in threads:
    thread.start()