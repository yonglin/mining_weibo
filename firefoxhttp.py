#coding=utf8
import urllib
import urllib2
import cookielib
import base64
import re
import json
import hashlib

COOKIE = 'SINAGLOBAL=9412320484407.246.1391513353463; wvr=5; un=zhuoylin@live.cn; YF-Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; SUS=SID-2123618881-1401684288-GZ-9qhz5-63c0b3c461c406c67d191c1cfdda208b; SUE=es%3D30118282a748066158359d247419f623%26ev%3Dv1%26es2%3D144f5256f3b45648fc8eac66904d4dbf%26rs0%3DaiTEsETyhRS47oizp7XoDS0nj2oGcTHhx1PsplmAz07d3%252BI4OKP8rZHExZoEyvD717RcCG7Y3X5Q9q9S2D4ASCwku9%252BxV5zaQV90OMA%252Bq7eCYwV%252BLOzsW9e5COutED7YFyt57sFCGdsJTOFoKqO6NaALilr8m7qLcydIceFF6Z8%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1401684288%26et%3D1401770688%26d%3Dc909%26i%3D208b%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D2123618881%26name%3Dzhuoylin%2540live.cn%26nick%3Dzhuoylin%26fmp%3D%26lcp%3D2012-12-06%252022%253A57%253A00; SUB=Afm6ARy%2FMUstzZxN5iA%2BszochYen00KH93jTOWf5HxC0o43Z7QETs%2FW%2FqCXiL54MX74lLfhLAkwmgE%2BkpjjNMCDjHmSF2A2KN3%2FU2XFmIlJ7FJPLaknkqAc3qbvHdgQ0E1mxlp9PTokWgWG2aKfB67A%3D; SUBP=002A2c-gVlwEm1uAWxfgXELuuu1xVxBxAAkT5EE38JjiTCzTR4yTQU2uHY-u_E%3D; ALF=1433220287; SSOLoginState=1401684288; YF-V5-G0=b1e3c8e8ad37eca95b65a6759b3fc219; _s_tentry=login.sina.com.cn; Apache=2418031105771.6606.1401684297739; ULV=1401684297753:158:2:2:2418031105771.6606.1401684297739:1401601972027; YF-Page-G0=0acee381afd48776ab7a56bd67c2e7ac; UOR=,,www.douban.com' 
HEADERS = {"cookie": COOKIE}
#获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
#将一个保存cookie对象,和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener,将保存了cookie的http处理器,还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#将包含了cookie,http处理器,http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)

postdata = {
    'entry': 'weibo',
    'gateway': '1',
    'from': '',
    'savestate': '7',
    'userticket': '1',
    'ssosimplelogin': '1',
    'vsnf': '1',
    'vsnval': '',
    'su': '',
    'service': 'miniblog',
    'servertime': '',
    'nonce': '',
    'pwencode': 'wsse',
    'sp': '',
    'encoding': 'UTF-8',
    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    'returntype': 'META'
}

def get_servertime():

    url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=dW5kZWZpbmVk&client=ssologin.js(v1.3.18)&_=1329806375939'
    data = urllib2.urlopen(url).read()
    p = re.compile('\((.*)\)')
    try:
        json_data = p.search(data).group(1)
        data = json.loads(json_data)
        servertime = str(data['servertime'])
        nonce = data['nonce']
        return servertime, nonce
    except:
        print 'Get severtime error!'
        return None

def get_pwd(pwd, servertime, nonce):
    pwd1 = hashlib.sha1(pwd).hexdigest()
    pwd2 = hashlib.sha1(pwd1).hexdigest()
    pwd3_ = pwd2 + servertime + nonce
    pwd3 = hashlib.sha1(pwd3_).hexdigest()
    return pwd3

def get_user(username):
    username_ = urllib.quote(username)
    username = base64.encodestring(username_)[:-1]
    return username

def main():
    username = 'www.crazyant.net'#微博账号
    pwd = 'xxxx'#微博密码
    url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.18)'
    try:
        servertime, nonce = get_servertime()
    except:
        return
    global postdata
    postdata['servertime'] = servertime
    postdata['nonce'] = nonce
    postdata['su'] = get_user(username)
    postdata['sp'] = get_pwd(pwd, servertime, nonce)
    postdata = urllib.urlencode(postdata)
    #其实到了这里,已经能够使用urllib2请求新浪任何的内容了,这里已经登陆成功了
    req  = urllib2.Request(
        url = url,
        data = postdata,
        headers = HEADERS
    )
    result = urllib2.urlopen(req)
    text = result.read()
    #print text
    p = re.compile('location\.replace\(\'(.*?)\'\)')
    try:
        login_url = p.search(text).group(1)
        print login_url
        #print login_url
        urllib2.urlopen(login_url)
        print "login success"
    except:
        print 'Login error!'
    #测试读取数据,下面的URL,可以换成任意的地址,都能把内容读取下来
    req = urllib2.Request(url='http://e.weibo.com/aj/mblog/mbloglist?page=1&count=15&max_id=3463810566724276&pre_page=1&end_id=3458270641877724&pagebar=1&_k=134138430655960&uid=2383944094&_t=0&__rnd=1341384513840',)
    result = urllib2.urlopen(req)
    text = result.read()
    print len(result.read())
    #unicode(eval(b),"utf-8")
    print eval("u'''"+text+"'''") 
main()