import requests
import datetime as dt
from RPi_GPIO_i2c_LCD import lcd
from time import strftime




url = f'http://api.openweathermap.org/data/2.5/weather?q={"ADD THE CITY YOU WANT"}&appid={"ADD YOUR OWN API KEY"}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['feels_like'] #2nd part can be changed to ['temp'] if you want the real temperature and not what it feels like
    temp -= 273.15 #if you are american search the conversion rate for fahrenheit instead of celsius
    tempC = int(temp)

    
else:
    print('error, data was not found')
         
print(f"{temp} C")

#test = "txt"

def MyFunction(self):
    self.lcd.display_string(str(strftime("%m/%d|%H:%M:%S")),1)
    self.lcd.display_string(str(strftime("%Y |Temp:" f"{tempC} C" )),2)  
    
    #self.lcd.display_string(test,2)
lcdDisplay=lcd.HD44780(0x27, MyFunction)
