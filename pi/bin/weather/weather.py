#!/usr/bin/python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json,urllib

#hangzhou url

hangzhou_weather = 'http://api.lib360.net/open/weather.json?city=%E6%9D%AD%E5%B7%9E'
json_weather = urllib.urlopen(hangzhou_weather).read()
weather_format = json.loads(json_weather)

completed_sentence=""

for everyday in weather_format['data']:
	month=everyday["Month"]
	day=everyday["Day"]
	weather=everyday["Weather"]
	maxtemp=everyday["TempMax"]
	mintemp=everyday["TempMin"]
	wind=everyday["Wind"]
	sentence1=str(month)+"月"+str(day)+"日  天气"+weather.encode('utf8')+"  最高温度"+str(maxtemp)+"度  最低温度"+str(mintemp)+"度  "+wind.encode('utf8')+"\n"
	completed_sentence += sentence1

for everyhour in weather_format['data24']:
	beginhour=everyhour["BeginHour"]
	endhour=everyhour["EndHour"]
	weather=everyhour["Weather"]
	maxtemp=everyhour["TempMax"]
	mintemp=everyhour["TempMin"]
	wind=everyhour["Wind"]
	sentence2='今日'+str(beginhour)+'点到'+str(endhour)+'点  天气'+weather.encode('utf8')+"  最高温度"+str(maxtemp)+"度  最低温度"+str(mintemp)+"度  "+wind.encode('utf8')+"\n";
	completed_sentence += sentence2

try:
	mintemp = weather_format['datanow']['TempMin']
	maxtemp = weather_format['datanow']['TempMax']
	weather = weather_format['datanow']['Weather']
	wind = weather_format['datanow']['Wind']
	pm25 = weather_format['pm25']
	sentence3='当前天气'+weather.encode('utf8')+"  最高温度"+str(maxtemp)+"度  最低温度"+str(mintemp)+"度  "+wind.encode('utf8')+"\n"
	completed_sentence += sentence3
except :
	pass

print completed_sentence
