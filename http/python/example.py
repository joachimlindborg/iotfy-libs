#!/usr/bin/env python

import iotfy


def example_function():
    client = iotfy.IotfyClient('12345', '5abc-4538a-97re', 'D12345', group="ABC")

    txt_response = client.send_txt_data("GPIO_40", "20")
    uart_response = client.send_txt_data("UART_1", "we-have-got-a-lot-of-data")
    gps_response = client.send_txt_data("GPS", "$GPGGA,092750.000,5321.6802,N,00630.3372,W,1,8,1.03,61.7,M,55.2,M,,*76")

    result = txt_response.read()
    if result == '0':
        print "Successful"
    else:
        print "Oh no ! It failed !"
        print result

    # Same handling for all other responses
