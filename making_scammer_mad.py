#make scammer mad
import os
import requests
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
url = 'http://heuiqgbqeifvqeqdvwrhbwtr.epizy.com/login.php'

names = json.loads(open('imiona.json').read())
for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahooyu.com'
    password = ''.join(random.choice(chars) for i in range(11))

    requests.post(url, allow_redirects=True, data={
        'email': username,
        'pass': password
    })
print('sending username: %s  sending password: %s ' % (username, password))
