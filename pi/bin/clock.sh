#!/bin/bash

Year=$(date +%Y)
Month=$(date +%m)
Day=$(date +%d)
Hour=$(date +%H)
Minute=$(date +%M)
Week=$(date +%u)

datestr=${Year}年${Month}月${Day}日
weekstr=星期${Week}
timestr=${Hour}点${Minute}分

#/usr/bin/curl --user-agent "Mozilla/5.0" "http://translate.google.cn/translate_tts?ie=UTF-8&q=${datestr}&tl=zh-CN&total=1&idx=0&textlen=2&client=t" > /tmp/date.out
#/usr/bin/curl --user-agent "Mozilla/5.0" "http://translate.google.cn/translate_tts?ie=UTF-8&q=${timestr}&tl=zh-CN&total=1&idx=0&textlen=2&client=t" > /tmp/time.out
#/usr/bin/curl --user-agent "Mozilla/5.0" "http://translate.google.cn/translate_tts?ie=UTF-8&q=${weekstr}&tl=zh-CN&total=1&idx=0&textlen=2&client=t" > /tmp/week.out

/usr/bin/curl --user-agent "Mozilla/5.0" "http://tts.baidu.com/text2audio?lan=zh&pid=101&ie=UTF-8&text=${datestr}&spd=2" > /tmp/date.out
/usr/bin/curl --user-agent "Mozilla/5.0" "http://tts.baidu.com/text2audio?lan=zh&pid=101&ie=UTF-8&text=${timestr}&spd=2" > /tmp/time.out
/usr/bin/curl --user-agent "Mozilla/5.0" "http://tts.baidu.com/text2audio?lan=zh&pid=101&ie=UTF-8&text=${weekstr}&spd=2" > /tmp/week.out

#/usr/bin/mplayer /tmp/date.out
#/usr/bin/mplayer /tmp/week.out
#/usr/bin/mplayer /tmp/time.out



/usr/bin/cvlc -R --no-repeat --play-and-exit --volume 165 /tmp/date.out
/usr/bin/cvlc -R --no-repeat --play-and-exit --volume 165 /tmp/week.out
/usr/bin/cvlc -R --no-repeat --play-and-exit --volume 165 /tmp/time.out
