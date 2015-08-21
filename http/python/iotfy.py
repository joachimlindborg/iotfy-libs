#!/usr/bin/env python

import json
import requests


class IotfyClient(object):

    # _api_path = "https://iotfy-ws.appspot.com/api/logger/v1"
    _api_path = "http://localhost:8080/api/logger/v1"
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

        response = requests.post(request_url, data=json.dumps(data), headers=headers)
        return response

    def upload_file(self, filename, mime_type, file_data, tag):
        upload_request_url = self._api_path + self._post_file_path
        headers = {'X-IOTFY-ID': self.uid, 'X-IOTFY-CLIENT': self.client_secret, 'Content-Type': 'application/json'}
        file_metadata = {'filename': filename, 'format': mime_type, 'tag': tag}
        upload_request_data = {'device': self.device_id, 'group': self.group, 'data': file_metadata}

        response = requests.post(upload_request_url, data=json.dumps(upload_request_data), headers=headers)
        if response.status_code != 200:
            return "ERROR ! Unable to get response from server"

        response_str = response.text
        response_dict = {}
        try:
            response_dict = json.loads(response_str)
        except ValueError, ve:
            return response

        upload_url = response_dict.get('url')
        upload_id = response_dict.get('id')

        files = {'file': (str(upload_id), file_data, mime_type)}

        upload_response = requests.post(upload_url, files=files)
        return upload_response
