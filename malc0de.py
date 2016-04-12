#!/usr/bin/env python
import untangle
import sys
import json
import re
import requests

def add_domain(d, i, com):
    # stolen from https://github.com/crits/crits/wiki/Authenticated-API
    url = 'http://localhost:8080/api/v1/domains/'
    data = {
        'api_key': 'a4eab72098c263d74d23e3745b361e910fe68ffa',
        'username': 'ckane',
        'source': 'malc0de',
        'reference': 'RSS feed',
        'method': 'malc0de.py',
        'domain': d,
        'ip': i,
        'ip_type': 'IPv4 Address',
        'ip_source': 'malc0de',
        'ip_reference': 'RSS feed',
        'ip_method': 'malc0de.py',
        'add_ip': True
    }
    r = requests.post(url, data=data)
    if r.status_code == 201:
        rj = json.loads(r.text)
        cdata = {
            'api_key': 'a4eab72098c263d74d23e3745b361e910fe68ffa',
            'username': 'ckane',
            'comment': com,
            'object_id': rj['id'],
            'object_type': 'Domain'
        }
        r = requests.post('http://localhost:8080/api/v1/comments', data=cdata)
        print "Successfully added " + data['domain']

data = untangle.parse('feed.xml')
ips = []
domains = []
ip_extr = re.compile('IP Address: (\\d+\\.\\d+\\.\\d+\\.\\d+)')
for item in data.rss.channel.item:
    ip_matches = ip_extr.search(item.description.cdata)
    ip = None
    if ip_matches:
        ip = ip_matches.group(1)
        add_domain(item.title.cdata, ip, item.description.cdata)
