import requests
import time
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from selenium import webdriver


#台北市
def Taipei_City():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rowsss = soup.find('table', attrs={'class':'FcstBoxTable01'})
    roe = rowsss.find_next('tbody')
    rows = roe.find_all('tr')
    content=[]
    aa="台北市天氣:"
    content.append(aa)
    for row in rows:
        times = row.find_next('th')
        temperatures = times.find_next('td')
        temperature = "溫度:"+temperatures.text
        re = temperatures.find_next('td')
        weather = re.find_next('img')
        weather = weather.get('title')
        weather = "天氣狀況:"+weather
        comforts = re.find_next('td')
        comfort = "舒適度:"+comforts.text
        rain = comforts.find_next('td')
        rain = "降雨機率:"+rain.text
        
        content.append(times.text)
        content.append(temperature)
        content.append(weather)
        content.append(comfort)
        content.append(rain)
        content.append("=========")
    return content

#台中市
def Taichung_City():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taichung_City.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rowsss = soup.find('table', attrs={'class':'FcstBoxTable01'})
    roe = rowsss.find_next('tbody')
    rows = roe.find_all('tr')
    content=[]
    aa="台中市天氣:"
    content.append(aa)
    for row in rows:
        times = row.find_next('th')
        temperatures = times.find_next('td')
        temperature = "溫度:"+temperatures.text
        re = temperatures.find_next('td')
        weather = re.find_next('img')
        weather = weather.get('title')
        weather = "天氣狀況:"+weather
        comforts = re.find_next('td')
        comfort = "舒適度:"+comforts.text
        rain = comforts.find_next('td')
        rain = "降雨機率:"+rain.text
        
        content.append(times.text)
        content.append(temperature)
        content.append(weather)
        content.append(comfort)
        content.append(rain)
        content.append("=========")
    return content

#台南市
def Tainan_City():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Tainan_City.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rowsss = soup.find('table', attrs={'class':'FcstBoxTable01'})
    roe = rowsss.find_next('tbody')
    rows = roe.find_all('tr')
    content=[]
    aa="台南市天氣:"
    content.append(aa)
    for row in rows:
        times = row.find_next('th')
        temperatures = times.find_next('td')
        temperature = "溫度:"+temperatures.text
        re = temperatures.find_next('td')
        weather = re.find_next('img')
        weather = weather.get('title')
        weather = "天氣狀況:"+weather
        comforts = re.find_next('td')
        comfort = "舒適度:"+comforts.text
        rain = comforts.find_next('td')
        rain = "降雨機率:"+rain.text
        
        content.append(times.text)
        content.append(temperature)
        content.append(weather)
        content.append(comfort)
        content.append(rain)
        content.append("=========")
    return content

#高雄市
def Kaohsiung_City():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Kaohsiung_City.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rowsss = soup.find('table', attrs={'class':'FcstBoxTable01'})
    roe = rowsss.find_next('tbody')
    rows = roe.find_all('tr')
    content=[]
    aa="高雄市天氣:"
    content.append(aa)
    for row in rows:
        times = row.find_next('th')
        temperatures = times.find_next('td')
        temperature = "溫度:"+temperatures.text
        re = temperatures.find_next('td')
        weather = re.find_next('img')
        weather = weather.get('title')
        weather = "天氣狀況:"+weather
        comforts = re.find_next('td')
        comfort = "舒適度:"+comforts.text
        rain = comforts.find_next('td')
        rain = "降雨機率:"+rain.text
        
        content.append(times.text)
        content.append(temperature)
        content.append(weather)
        content.append(comfort)
        content.append(rain)
        content.append("=========")
    return content

#新竹市
def Hsinchu_City():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_City.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rowsss = soup.find('table', attrs={'class':'FcstBoxTable01'})
    roe = rowsss.find_next('tbody')
    rows = roe.find_all('tr')
    content=[]
    aa="新竹市天氣:"
    content.append(aa)
    for row in rows:
        times = row.find_next('th')
        temperatures = times.find_next('td')
        temperature = "溫度:"+temperatures.text
        re = temperatures.find_next('td')
        weather = re.find_next('img')
        weather = weather.get('title')
        weather = "天氣狀況:"+weather
        comforts = re.find_next('td')
        comfort = "舒適度:"+comforts.text
        rain = comforts.find_next('td')
        rain = "降雨機率:"+rain.text
        
        content.append(times.text)
        content.append(temperature)
        content.append(weather)
        content.append(comfort)
        content.append(rain)
        content.append("=========")
    return content

#桃園市
def Taoyuan_City():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taoyuan_City.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rowsss = soup.find('table', attrs={'class':'FcstBoxTable01'})
    roe = rowsss.find_next('tbody')
    rows = roe.find_all('tr')
    content=[]
    aa="桃園市天氣:"
    content.append(aa)
    for row in rows:
        times = row.find_next('th')
        temperatures = times.find_next('td')
        temperature = "溫度:"+temperatures.text
        re = temperatures.find_next('td')
        weather = re.find_next('img')
        weather = weather.get('title')
        weather = "天氣狀況:"+weather
        comforts = re.find_next('td')
        comfort = "舒適度:"+comforts.text
        rain = comforts.find_next('td')
        rain = "降雨機率:"+rain.text
        
        content.append(times.text)
        content.append(temperature)
        content.append(weather)
        content.append(comfort)
        content.append(rain)
        content.append("=========")
    return content

#屏東縣
def Pingtung_County():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Pingtung_County.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rowsss = soup.find('table', attrs={'class':'FcstBoxTable01'})
    roe = rowsss.find_next('tbody')
    rows = roe.find_all('tr')
    content=[]
    aa="屏東縣天氣:"
    content.append(aa)
    for row in rows:
        times = row.find_next('th')
        temperatures = times.find_next('td')
        temperature = "溫度:"+temperatures.text
        re = temperatures.find_next('td')
        weather = re.find_next('img')
        weather = weather.get('title')
        weather = "天氣狀況:"+weather
        comforts = re.find_next('td')
        comfort = "舒適度:"+comforts.text
        rain = comforts.find_next('td')
        rain = "降雨機率:"+rain.text
        
        content.append(times.text)
        content.append(temperature)
        content.append(weather)
        content.append(comfort)
        content.append(rain)
        content.append("=========")
    return content

#花蓮縣
def Hualien_County():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Hualien_County.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rowsss = soup.find('table', attrs={'class':'FcstBoxTable01'})
    roe = rowsss.find_next('tbody')
    rows = roe.find_all('tr')
    content=[]
    aa="花蓮縣天氣:"
    content.append(aa)
    for row in rows:
        times = row.find_next('th')
        temperatures = times.find_next('td')
        temperature = "溫度:"+temperatures.text
        re = temperatures.find_next('td')
        weather = re.find_next('img')
        weather = weather.get('title')
        weather = "天氣狀況:"+weather
        comforts = re.find_next('td')
        comfort = "舒適度:"+comforts.text
        rain = comforts.find_next('td')
        rain = "降雨機率:"+rain.text
        
        content.append(times.text)
        content.append(temperature)
        content.append(weather)
        content.append(comfort)
        content.append(rain)
        content.append("=========")
    return content

#台東縣
def Taitung_County():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taitung_County.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rowsss = soup.find('table', attrs={'class':'FcstBoxTable01'})
    roe = rowsss.find_next('tbody')
    rows = roe.find_all('tr')
    content=[]
    aa="臺東縣天氣:"
    content.append(aa)
    for row in rows:
        times = row.find_next('th')
        temperatures = times.find_next('td')
        temperature = "溫度:"+temperatures.text
        re = temperatures.find_next('td')
        weather = re.find_next('img')
        weather = weather.get('title')
        weather = "天氣狀況:"+weather
        comforts = re.find_next('td')
        comfort = "舒適度:"+comforts.text
        rain = comforts.find_next('td')
        rain = "降雨機率:"+rain.text
        
        content.append(times.text)
        content.append(temperature)
        content.append(weather)
        content.append(comfort)
        content.append(rain)
        content.append("=========")
    return content