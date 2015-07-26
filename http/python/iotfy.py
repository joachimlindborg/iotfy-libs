#!/usr/bin/env python

import json
import urllib2


class IotfyClient(object):

    _base_url = "http://iotfy-ws.appspot.com"
    _send_txt_url = "/d/send_txt_data"

    def __init__(self, uid, client_secret, device_id, group=None):
        self.uid = uid
        self.client_secret = client_secret
        self.device_id = device_id
        self.group = group

    def send_txt_data(self, tag, data):
        headers = {'X-IOTFY-ID': self.uid, 'X-IOTFY-CS': self.client_secret, 'Content-Type': 'application/json'}
        data = {'device': self.device_id, 'group': self.group, 'tag': tag, 'data': data}
        request_url = self._base_url + self._send_txt_url

        request = urllib2.Request(request_url, json.dumps(data), headers)
        response = urllib2.urlopen(request)
        return response
