import requests
from subprocess import Popen,PIPE
import re
import threading

with open('url.txt') as li:
    arr = li.readlines()
    array = []
    for i in arr:
        i = i.strip('\n')
        array.append(i)

for i in array:
    j = ''.join(i)
    def pings():
        ping = Popen(['/bin/bash','-c','ping -c 1 ' + j],stdin=PIPE,stdout=PIPE)
        data = ping.stdout.read()
        db = str(data)
        result = re.findall(r'\d+.\d+.\d+.\d+', db)
        ip = result[0]
        ips = 'http://' + str(ip) + ':888/pma/'
        try:
            dd = requests.get(ips , timeout=3)
            print(dd.status_code)
            print(ips)

        except Exception:
            print('连接失败')
            print(ips)

    for i in range(1):
        t = threading.Thread(target=pings)
        t.start()