#!/usr/bin/env python

import iotfy
import mimetypes


def text_data_logger_example():
    client = iotfy.IotfyClient('1234567890', '123-456-abcd-789', 'D123', group="ABC")

    data = []

    data.append({"tag": "GPIO_40, temperature-sensor", "text": "20"})
    data.append({"tag": "UART_1", "text": "Lots of data for you"})

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


def file_upload_example():
    client = iotfy.IotfyClient('1234567890', '123-456-abcd-789', 'D123', group="ABC")

    filename = "sample.jpg"
    with open(filename, "rb") as f:
        upload_response = client.upload_file(filename, mimetypes.guess_type(filename)[0], f.read(), "hello, blob")
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
    text_data_logger_example()
    file_upload_example()
