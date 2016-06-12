#!/bin/bash

datastr=$(/usr/bin/python /home/pi/bin/weather/weather.py)

print $datastr

for str in `echo $datastr`
do
	/usr/bin/curl --user-agent "Mozilla/5.0" "http://tts.baidu.com/text2audio?lan=zh&pid=101&ie=UTF-8&text=${str}&spd=2" > date.out
	/usr/bin/mplayer date.out
done
