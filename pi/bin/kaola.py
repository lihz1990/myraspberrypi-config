#!/usr/bin/python
#vim: set fileencoding:utf-8
#-*-coding:utf-8 -*-
#coding:utf-8

import pycurl
import os
import StringIO
import re


KAOLA_LOGIN_URI = 'https://reg.163.com/logins.jsp'
KAOLA_LOGIN_REFERER = 'http://www.kaola.com/'
KAOLA_SIGN_URI = 'http://www.kaola.com/personal/my_sign.html'
KAOLA_SIGN_REFERER = 'http://www.kaola.com/'
COOKIE_DIR = '/tmp/cookies/'

def xCurl(url, returndata=True, postData=None, cookiePath=None, referer=None,
    userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.xCurl(url, return=True, postData=null, cookiePath=null, referer=null, proxy=[], user|36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"):
    ch = pycurl.Curl()
    fc = StringIO.StringIO()

    ch.setopt(pycurl.AUTOREFERER, 1)
    ch.setopt(pycurl.URL, url)
    ch.setopt(pycurl.HEADER, 0)
    ch.setopt(pycurl.WRITEFUNCTION, fc.write)
    ch.setopt(pycurl.TIMEOUT, 20)
    ch.setopt(pycurl.CONNECTTIMEOUT, 10)
    ch.setopt(pycurl.SSL_VERIFYPEER, False)
    ch.setopt(pycurl.SSL_VERIFYHOST, False)

    if referer:
        ch.setopt(pycurl.REFERER, referer)
    if userAgent:
        ch.setopt(pycurl.USERAGENT, userAgent)
    if cookiePath:
        ch.setopt(pycurl.COOKIEFILE, cookiePath)
        ch.setopt(pycurl.COOKIEJAR, cookiePath)
    if postData:
        ch.setopt(pycurl.POST, 1)
        ch.setopt(pycurl.POSTFIELDS, postData)

    try:
        ch.perform()
        content = fc.getvalue()
    except pycurl.error, error:
        errno, errstr =error

    ch.close()
    if returndata:
        return content
    else:
        print content

def kaola_login(account, cookie_path, kaola_cookie_path):
    if not  account['username'] or not account['password']:
        return False
    
    account['url'] = 'http://global.163.com/urs/redirect.html?username=' + account['username'].split('@')[0] + '&target=http://www.kaola.com/agent/loginAgjent.htm?from=iframeLogin'
    account['url2'] = 'http://www.kaola.com/personal/my_sign.html'
    account['savelogin'] = 1
    account['domains'] = 'kaola.com,163.com'
    account['noRedirect'] = 0
    post_data = '';

    for k in account:
        post_data = post_data + k + "=" + str(account[k]) + "&"

    content = xCurl(KAOLA_LOGIN_URI, True, post_data, cookie_path, KAOLA_LOGIN_REFERER)
    if 'hidden">登录成功' not in content:
        content = xCurl(KAOLA_LOGIN_URI, True, post_data, cookie_path, KAOLA_LOGIN_REFERER)    
        if 'hidden">登录成功' not in content:
            return False

    content = xCurl(account['url'], True, None, cookie_path)
    patt = re.compile(r'http:\/\/www\.kaola\.com\/urs\/setUrsCookie\.html.+')
    setcookie_url = patt.findall(content)
    #match = re.match('(http://www.kaola.com/urs/setUrsCookie.html', content)
    if not setcookie_url:
        print "SetCookie content empty"
        exit(1)
    if not setcookie_url[0]:
        print 'Match kaola set cookie URL failed'
        exit(1)
    content = xCurl(setcookie_url[0], True, None, kaola_cookie_path)
    return True

def kaola_sign(account, cookie_path):
    kaola_cookie_path = cookie_path + '_kaola.txt'
    #os.unlink(kaola_cookie_path)
    #os.unlink(cookie_path)
    
    if not (kaola_login(account, cookie_path, kaola_cookie_path)):
        kaola_login(account, cookie_path, kaola_cookie_path)
    
    content = xCurl(KAOLA_SIGN_URI, True, None, kaola_cookie_path, KAOLA_SIGN_REFERER)
    if '"msg":"签到成功"' in content:
        return True
    else:
        return False


account = {}
account['username'] = 'graylc@163.com'
account['password'] = 'graylc@netease'

cookie_path = COOKIE_DIR + account['username']

if not os.path.isdir(COOKIE_DIR):
    os.mkdir(COOKIE_DIR)
    

if kaola_sign(account, cookie_path):
    print "sign ok"
else:
    print "sign failed"


