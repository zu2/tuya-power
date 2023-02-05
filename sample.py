#!/usr/bin/env python3

import tuyapower
import tinytuya
import json

devices_json = json.load(open('devices.json','r'))
devices = tuyapower.deviceScan()
print(devices)
for ip in devices:
    id = devices[ip]['gwId']
    k1 = list(filter(lambda k: k['id']==id, devices_json))
    if not k1:
        break
    key = k1[0]['key']
    vers = devices[ip]['version']
    (on, w, mA, V, err) = tuyapower.deviceInfo(id, ip, key, vers)
    print("Device at %s: ID %s, state=%s, W=%s, mA=%s, V=%s [%s]"%(ip,id,on,w,mA,V,err))
