#!/usr/bin/env python3

"""Munin plugin for tuya device power status

=head1 NAME

tuya-munin.py

=head1 APPLICABLE SYSTEMS

##  TBD

=head1 CONFIGURATION

## TBD

=head1 INTERPRETATION

## TBD

=head1 AUTHOR

zu2@twitter

=head1 LICENSE

## TBD

=head1 MAGIC MARKERS

# #%# family=auto
# #%# capabilities=autoconf

=cut
"""

import os
import sys
import tuyapower
import tinytuya
import json

devices_json = json.load(open('devices.json','r'))


def config():
    """Print plugin config."""
    print('multigraph tuya_mA')
    print('graph_title tuya mA')
    print('graph_vlabel mA')
    print('graph_category power')
    print('graph_args --base 1000 --lower-limit 0')
    for ip in devices_json:
        #name = devices_json['ip']['name']
        name = ip['name']
        id   = ip['id']
        print('mA_%s.label %s'%(id,name))

    print('multigraph tuya_W')
    print('graph_title tuya W')
    print('graph_vlabel W')
    print('graph_category power')
    print('graph_args --base 1000 --lower-limit 0')
    for ip in devices_json:
        name = ip['name']
        id   = ip['id']
        print('W_%s.label %s'%(id,name))
    if os.environ.get('MUNIN_CAP_DIRTYCONFIG') == '1':
       fetch()


def fetch():
    """Print values."""
    devices = tuyapower.deviceScan()
    power = []
    for ip in devices:
        id = devices[ip]['gwId']
        k1 = list(filter(lambda k: k['id']==id, devices_json))
        if not k1:
            continue
        key = k1[0]['key']
        vers = devices[ip]['version']
        (on, w, mA, V, err) = tuyapower.deviceInfo(id, ip, key, vers)
        power.append( {'gwId':id, 'on': on, 'w': w, 'mA': mA, 'V': V, 'err': err } );

    print('multigraph tuya_mA')
    for p in power:
        if p['err'] != 'OK':
            continue
        print('mA_%s.value %s'%(p['gwId'],p['mA']))

    print('multigraph tuya_W')
    for p in power:
        if p['err'] != 'OK':
            continue
        print('W_%s.value %s'%(p['gwId'],p['w']))

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'autoconf':
        print('yes')
    elif len(sys.argv) > 1 and sys.argv[1] == 'config':
        config()
    else:
        fetch()
