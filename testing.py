




import datetime

import pytz

import pytz


current_utc = datetime.datetime.now(pytz.timezone('Asia/Baghdad')).strftime("%H:%M:%S")
print(current_utc)

import urllib3
import json
url="http://127.0.0.1:8000/test"
    

http = urllib3.PoolManager()
r = http.request(
   'POST',
    url,
)
print(r.data.decode('utf-8'))
#print (json.loads(r.data.decode('utf-8')))
