#!/usr/bin/env python
import urllib2
import datetime

postData = 'curl -X POST -d "{\"nama_perangkat\": \"coba1\", \"pemakaian_daya\": \"10\"}" -H "Content-Type: application/json" http://localhost:3000/api/sensor'

idSensor = 2
nilai = 100
head = 'iotpln2016'
datetime = datetime.date.today()
data = '{"datetime":"'+str(datetime)+'","id_sensor": "'+str(idSensor)+'","nilai_sensor":"'+str(nilai)+'","header":"'+str(head)+'"}'
url = 'http://agungdp.agri.web.id:3456/api/sensor'
req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
f = urllib2.urlopen(req)
for x in f:
    print(x)
f.close()

print data