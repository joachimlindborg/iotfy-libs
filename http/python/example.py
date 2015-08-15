#!/usr/bin/env python

import iotfy


def text_data_logger_example():
    client = iotfy.IotfyClient('12345', '5abc-4538a-97re', 'D123', group="ABC")

    data = []

    data.append({"tag": "GPIO_40, temperature-sensor", "text": "20"})
    data.append({"tag": "UART_1", "text": "Lots of data for you"})

    response = client.post_text_data(data)
    if response.code != 200:
        print "ERROR !"
    else:
        result = response.read()
        if result == '0':
            print "Successful"
        else:
            print "Oh no ! It failed !"
            print result


def file_upload_example():
    client = iotfy.IotfyClient('12345', '5abc-4538a-97re', 'D123', group="ABC")

    filename = "README.md"
    with open(filename, "rb") as f:
        upload_response = client.upload_file(filename, "text/plain", f.read(), "hello, blob")
        if upload_response.code != 200:
            print "ERROR !"
        else:
            result = upload_response.read()
            if result == '0':
                print "Upload Successful"
            else:
                print "Oh no ! It failed !"
                print result
