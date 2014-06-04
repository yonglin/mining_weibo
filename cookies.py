#coding=utf8

import urllib2
import re
import nltk 
import pickle
"""
Login to Sina Weibo with cookie
"""

COOKIE = 'SINAGLOBAL=9412320484407.246.1391513353463; wvr=5; un=zhuoylin@live.cn; YF-Ugrow-G0=9e7ca4c96e5e7034874e5b22c95ae5e5; SUS=SID-2123618881-1401837334-GZ-ng6ur-cb2441c0b3e8fa29a9d84aa6e230208b; SUE=es%3D2e1ca2261375f361510058a50d04d3e5%26ev%3Dv1%26es2%3Daa21780adc29e1d40cc362dc1cb6a42c%26rs0%3DBKRDv1pkyqWXz13xL8JXpEursTzPNUt7mOF%252BB%252FAh%252F%252BYXJzlW%252FWNyi1v9KvfvT8fLQ9wxFhwOMEKShqP%252BkDVwqO%252FSjCn4w2IIXjBXppDfYzcudhQZMcTE9LADL3YW%252FVgDKLLUbAFj%252BFOoiAf0bz3qecTCGpw31duGfcUTnSPDIqA%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1401837334%26et%3D1401923734%26d%3Dc909%26i%3D208b%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D2123618881%26name%3Dzhuoylin%2540live.cn%26nick%3Dzhuoylin%26fmp%3D%26lcp%3D2012-12-06%252022%253A57%253A00; SUB=AchbdRbpUJZLU3YOPJtXmQCX6T5tvxRD%2FYepCP33S0Zcb0mkKLhbb7RExm8UVWqPIk%2BYgJM1Vb%2Fx%2BewwUt3a41it3gYza4LJ2qeHoz4zhF3Tc4WcjQi9OVNSKPr4PbEGqFvvTpuLDHnLOISvJgCINbI%3D; SUBP=002A2c-gVlwEm1uAWxfgXELuuu1xVxBxAAkT5EE38JjiTCzTR4yTQU2uHY-u_E%3D; ALF=1433373331; SSOLoginState=1401837334; YF-V5-G0=f7add382196ce7818cd5832b5a20aaf5; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=9416516376659.273.1401837348921; ULV=1401837349019:160:4:4:9416516376659.273.1401837348921:1401769862681'

#fill with your weibo.com cookie
HEADERS = {"cookie": COOKIE}

def test_login(url):
    #url = 'http://s.weibo.com/wb/%E5%BC%A0%E5%8D%83%E5%B8%86&xsort=hot'
    req = urllib2.Request(url, headers=HEADERS)
    r = urllib2.urlopen(req)
    web_page = r.read()
    #desc = nltk.clean_html(text)
    print "1"
    return web_page
    #pat_title = re.compile('<title>(.+?)</title>')
    #r = pat_title.search(text)
    #if r:
        #print r.group(1)

def keep_data(address,raw_data):
	'''using pickle to store the raw data'''

	filename = address
	data = raw_data
	f = open(filename, 'wb')
	pickle.dump(data, f) # dump the object to a file
	f.close()

def get_data(address):
	'''using pickle to get the raw data'''

	f = open(address, 'rb')
	data = pickle.load(f) # load the object from the file
	f.close()
	return data
	
