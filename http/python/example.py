#!/usr/bin/env python

import iotfy
import mimetypes


def iotfy_text_data_log():
    client = iotfy.IotfyClient('5910602190946304', '63609510-acd3-488d-a304-914b198827b7', 'C1_D1', group="Omno_GoJavas")

    data = []

    data.append({"tag": "CAM_2", "text": "Unusual"})

    response = client.post_text_data(data)
    if response.status_code != 200:
        print "ERROR !"
    else:
        result = response.text
        if result == '0':
            print "Successful"
        else:
            print "Oh no ! It failed !"
            print result


def iotfy_file_uploader(fname):
    #client = iotfy.IotfyClient('1234567890', '123-456-abcd-789', 'D123', group="ABC")
    client = iotfy.IotfyClient('5910602190946304', '63609510-acd3-488d-a304-914b198827b7', 'C1_D2', group="Omni_GoJavas")

    filename = fname
    with open(filename, "rb") as f:
        upload_response = client.upload_file(filename, mimetypes.guess_type(filename)[0], f.read(), "Occlusion")
        if upload_response.status_code != 200:
            print "ERROR !"
        else:
            result = upload_response.text
            if result == '0':
                print "Upload Successful"
            else:
                print "Oh no ! It failed !"
                print result


if __name__ == '__main__':
    #iotfy_text_data_log()
    iotfy_file_uploader('07082015_0415_1_cam0.avi')
