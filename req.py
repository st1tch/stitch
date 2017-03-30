import requests
import md5
import sys

def login(type_, payload={}):
    if type_ == 'post':
        return requests.post(url, data=payload)
    elif type_ == 'get':
        return requests.get(url, params=payload)
    else:
        print 'login type error'

def login_cookie(type_, header):
    if type_ == 'get':
        return requests.get(url, headers=header)
    elif type_ == 'post':
        return requests.get(url, headers=header)
    else:
        print 'login cookie type error'

def recv_data(type_, payload={}, header={}):
    if type_ == 'get':
        return requests.post(url, data=payload, headers=header)
    elif type_ == 'post':
        return requests.get(url, data=payload, headers=header)
    else:
        print 'type error'

def get_payload(pay):
    result = {}
    for dat in pay.split('&'):
        k, v = dat.split('=')
        result[k] = v
    return result

if __name__ == "__main__":
    url = 'http://wargame.kimtae.xyz/certis-ctf/'
    #login test
    payload = get_payload('target=login&oper=signin&ajax=true&id=&pw=')
    payload['id']='stitch'
    payload['pw']=md5.new('12345').digest().encode('hex')
    k = login('post', payload)
    #print k.text

    #cookie login test
    header = {'Cookie':k.headers['Set-Cookie']}
    k = login_cookie('post', header)
    #print k.text

    #move rank
    payload = {
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Accept':'text/plain, */*; q=0.01',
	'X-Requested-With':'XMLHttpRequest',
	'Referer':'http://wargame.kimtae.xyz/certis-ctf/',
	'Accept-Language': 'ko-KR',
	'Accept-Encoding': 'gzip, deflate',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
	'Content-Length': '11',
	'Host': 'wargame.kimtae.xyz',
	'Connection': 'Keep-Alive',
	'Pragma': 'no-cache',
    }
    payload['target'] = 'rank'
    k = recv_data('post', payload, header)
    print k.text
