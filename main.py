
import requests
import os

ltuid = os.environ.get('LTUID')
ltoken = os.environ.get('LTOKEN')

url = "https://api-os-takumi.mihoyo.com/event/mani/sign?act_id=e202110291205111&lang=ko-kr"

cookies = {'ltuid': ltuid, 'ltoken': ltoken}

r = requests.post(url, cookies=cookies)
print(r.json()['message'])
