import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import html5lib
from sys import version_info
from unicornhelper import *

def weather_url():
    py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2
    if py3:
        Zip_Code = input("Please Enter a Zip Code: ").strip().replace(' ','').split('-')[0]
        assert len(Zip_Code) == 5
        assert Zip_Code.isnumeric()
    else:
        print('Wrong version of Python!\nTry again with Python 3.x')
    url = 'https://weather.com/weather/hourbyhour/l/%s:4:US' %(Zip_Code)
    return(url)

def get_weather_df(zip_code):
    Zip_Code = zip_code.strip().replace(' ','').split('-')[0]
    if len(Zip_Code) == 5 and Zip_Code.isnumeric():
        url = 'https://weather.com/weather/hourbyhour/l/%s:4:US' %(Zip_Code)
    else:
        url = weather_url()

    temp_df = pd.read_html(url)[0]
    temp_df = temp_df.iloc[:,1:]
    temp_df.columns = ['Time','Description','Temp','Feels','Precip','Humidity','Wind']
    temp_df['Time'] = pd.to_datetime(temp_df['Time'])
    temp_df['Temp'] = temp_df['Temp'].map(lambda x: int(x[:-1]))
    temp_df['Feels'] = temp_df['Feels'].map(lambda x: int(x[:-1]))
    temp_df['Precip'] = temp_df['Precip'].map(lambda x: int(x[:-1]))
    temp_df['Humidity'] = temp_df['Humidity'].map(lambda x: int(x[:-1]))
    temp_df['Wind Direction'] = temp_df['Wind'].map(lambda x: x.split()[0])
    temp_df['Wind Speed'] = temp_df['Wind'].map(lambda x: x.split()[1])
    temp_df.index.name=''
    temp_df.index=(temp_df['Time'])
    temp_df = temp_df[['Description','Temp','Feels','Precip','Humidity','Wind Direction','Wind Speed']]
    return (temp_df)

#weather func
#temp-bar
def set_temp(temp):
    temp = int(temp)
    
    def linshuffle(linspace,temp):
        ticks = linspace
        tmp = temp
        ticks.put(0,int(tmp))
        ticks.sort()
        ticks = pd.Series(ticks)
        return (ticks[ticks == temp].index[0])
        
    if int(temp) <= 32:
        T = linshuffle(np.linspace(0,32,8),temp)
        L = int(np.ceil(temp * 8/32))
        R,G,B = (0,0,100)
        set_hpline([0],L,R,G,B)
    elif int(temp) < 75:
        T = linshuffle(np.linspace(32,75,8),temp)
        L = int(np.ceil(temp * 8 /75))
        R,G,B = (0,int(np.ceil(3*int(temp))),0)
        set_hpline([0],L,R,G,B)
    elif int(temp) >= 75:
        T = linshuffle(np.linspace(75,100,8),temp)
        L = int(np.ceil(temp * 1/6) - 9)
        R,G,B = (2*int(temp),0,0)
        set_hpline([0],L,R,G,B)
    
#humidity-bar
def set_humidity(hum):
    humidity = int(hum)
    L = min(int(np.ceil(humidity * 8 / 100)), 8)
    R,G,B = (0,85,max(2*humidity,175))
    set_hpline([1],L,R,G,B)
    
#precipitation-bar
def set_precipitation(precip):
    precipitation = int(precip)
    L = min(int(np.ceil(precipitation * 8 / 100)), 8)
    R,G,B = (0,0,min(int(np.ceil(12 * precipitation)),200))
    #L = int(L)
    set_hpline([2],L,R,G,B)
    
#windspeed-bar
def set_windspeed(wspeed):
    wind_speed = int(wspeed)
    L = min(int(np.ceil(np.log2(wind_speed))), 8)
    R,G,B = (100,100,100)
    set_hpline([3],L,R,G,B)
    
def weatherset(zip_code):
    Zip_Code = zip_code
    if len(Zip_Code) == 5 and Zip_Code.isnumeric():
        temp_df = get_weather_df(Zip_Code)
    else:
        temp_df = get_weather_df('10014')
    #temp_df = get_weather_df(Zip_Code)
    current_weather = temp_df.iloc[0]
    uh_reset()
    set_temp(current_weather['Temp'])
    set_humidity(current_weather['Humidity'])
    set_precipitation(current_weather['Precip'])
    set_windspeed(current_weather['Wind Speed'])
   
    
def weatherloop(zip_code,n):
    """
    n defaults to 20,  zip_code needs valid zip code
    """
    uh_reset()
    if n.isnumeric():
        n = int(n)
    else:
        n = 20
    Zip_Code = zip_code.strip().replace(' ','').split('-')[0]
    if n == 0:
        while True:
            weatherset(Zip_Code)
    else:
        for i in range(int(n)):
            weatherset(Zip_Code)
            time.sleep(5)

def getzip():
    while True:
        py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2
        if py3:
            Zip_Code = input("Please Enter a Zip Code: ").strip().replace(' ','').split('-')[0]
            assert len(Zip_Code) == 5
            assert Zip_Code.isnumeric()
            return(Zip_Code)
        else:
            print('Wrong version of Python!\nTry again with Python 3.x')
            break
            
def getn():
    while True:
        py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2
        if py3:
            n = input("Please enter an integer: ").strip().replace(' ','').split('-')[0]
            return (n)
        else:
            print ('error! enter a vaid integer!')
            break
def main():
    zip_code = getzip()
    n = getn()
    weatherloop(zip_code,n)
    
if __name__ == "__main__":
    main()
