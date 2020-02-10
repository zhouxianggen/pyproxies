import requests


url = 'https://soccer.hupu.com/'
r = requests.get(
        'https://soccer.hupu.com/', 
        proxies={'HTTP': 'http://127.0.0.1:8808'})
print(r.status_code)
