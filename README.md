# YouTubeBot



### Youtubebot.py

```
from selenium import webdriver
import time


number_of_drivers = int(input("Enter the number of drivers : " ))
time_to_refresh = int(input("Enter refresh rate time in seconds : " ))
url = input("Enter URL : " )
drivers =[]

for i in range(number_of_drivers):
    drivers.append(webdriver.Chrome(executable_path = "chromedriver"))
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(number_of_drivers):
        drivers[i].refresh()
        
```

### YTBot.py


```
import webbrowser, time


url = input("Enter url: ")
views = input("Enter amount of views: ")
duration = input("Enter duration before opening another video (in seconds): ")

for i in range(int(views)):
    webbrowser.open_new(url)
    time.sleep(int(duration))
    
```    

P.S: 
* You needs [webdriver](https://chromedriver.chromium.org/downloads). webdriver must match with your chrome version.
* Update EnvPath:
* >C:\Program Files\webdrivers\    || chromedriver.exe
* Install selenium
* >pip install selenium
