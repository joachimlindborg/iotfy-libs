#!/usr/bin/env python

import json
import urllib2

import utils


class IotfyClient(object):

    _api_path = "https://iotfy-ws.appspot.com/api/logger/v1"
    _post_txt_path = "/post_text_data"
    _post_file_path = "/post_file_info"

    def __init__(self, uid, client_secret, device_id, group=None):
        self.uid = uid
        self.client_secret = client_secret
        self.device_id = device_id
        self.group = group

    def post_text_data(self, data):
        request_url = self._api_path + self._post_txt_path
        headers = {'X-IOTFY-ID': self.uid, 'X-IOTFY-CLIENT': self.client_secret, 'Content-Type': 'application/json'}
        data = {'device': self.device_id, 'group': self.group, 'data': data}

        request = urllib2.Request(request_url, json.dumps(data), headers)
        response = urllib2.urlopen(request)
        return response

    def upload_file(self, filename, mime_type, file_data, tag):
        upload_request_url = self._api_path + self._post_file_path
        headers = {'X-IOTFY-ID': self.uid, 'X-IOTFY-CLIENT': self.client_secret, 'Content-Type': 'application/json'}
        file_metadata = {'filename': filename, 'format': mime_type, 'tag': tag}
        upload_request_data = {'device': self.device_id, 'group': self.group, 'data': file_metadata}

        request = urllib2.Request(upload_request_url, json.dumps(upload_request_data), headers)
        response = urllib2.urlopen(request)
        if response.code != 200:
            return "ERROR ! Unable to get response from server"

        response_str = response.read()
        response_dict = {}
        try:
            response_dict = json.loads(response_str)
        except ValueError, ve:
            return response

        upload_url = response_dict.get('url')
        upload_id = response_dict.get('id')

        # Encode file to multipart form data and upload it !
        content_type, body = utils.encode_multipart_formdata(file_data, mime_type, upload_id)
        upload_file_headers = {'Content-Type': content_type}
        upload_request = urllib2.Request(upload_url, body, upload_file_headers)
        upload_response = urllib2.urlopen(upload_request)

        return upload_response
