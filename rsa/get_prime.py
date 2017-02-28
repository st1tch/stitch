import requests
import re
import sys

def finder():
    try:
        n = int(sys.argv[1], 16)
        url_1 = 'http://www.factordb.com/index.php?query=%i'
        url_2 = 'http://www.factordb.com/index.php?id=%s'
        r = requests.get(url_1 % n)
        regex = re.compile("index\.php\?id\=([0-9]+)", re.IGNORECASE)
        ids = regex.findall(r.text)
        p_id = ids[1]
        q_id = ids[2]
        regex = re.compile("value=\"([0-9]+)\"", re.IGNORECASE)
        r_1 = requests.get(url_2 % p_id)
        r_2 = requests.get(url_2 % q_id)
        p = int(regex.findall(r_1.text)[0])
        q = int(regex.findall(r_2.text)[0])
        if p == q == n:
            print 'nono'
            return
        print p, q
    except:
        print 'nono'
        return

if __name__ == '__main__':
    finder()
