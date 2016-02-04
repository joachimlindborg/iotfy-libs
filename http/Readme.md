The telemetry api runs over HTTPS and is useful for logging device data (sensor data/file etc) to Iotfy cloud.
Once you add a device from Iotfy's web panel, you will get a X-IOTFY-ID and X-IOTFY-CLIENT of the new device on the panel.
These will be used as headers in the HTTPS calls below.

Below are the details of the api call:

####URL: https://cloud.iotfy.co/api/telemetry/v1/post_text_data

Type: HTTP POST

Description: This API can be use to log sensor data to the cloud.
Add X-IOTFY-ID, X-IOTFY-CLIENT and Content-Type in the header of the call.
The call body is a json in the format below:

`{
    "device":"D1",
    "group":"TEST_DEVICES",
    "data": [
                {
                    "tag": "GPIO_41, temperature",
                    "text": "52"
                },
                {
                    "tag": "current",
                    "text": "2"
                }
            ]
}`

device - It is the name or the ID you would like to give to the device.

group - Name of the deployment group, the device is part of.

data - It is the list of (tag, text) pairs which you can send for logging to the cloud server.<br/>

    tag - It provides context to the data you want to log. You can also search data in the panel via tag values. If there are multiple tags associated with a single value you can separate them with a comma.
    text - This denotes the value which needs to be logged on the server.
 
See the python example as a guide to how to use this call.

=====================================================================================================================================

####URL: https://cloud.iotfy.co/api/telemetry/v1/post_file_info

Type: HTTP POST

Description: This API can be use to log files to the cloud and it works in a different way slightly different way than the text logging call. Add X-IOTFY-ID, X-IOTFY-CLIENT and Content-Type in the header of the call.
The call body is a json in the format below:

`{
    "device":"D2",
    "group":"TEST_DEVICES",
    "data": {"filename": "file_name", "format": "file_mime_type", "tag": "motion_detected"}
}`

data - In this call, the data key contains the following key/values:<br/>

    filename: The name of the file you are uploading
    format: A valid mime type of the file (See the python code for more details)
    tag: This is same as above and provides context to the file you want to log
        
After this call is successful, the response contains an upload_url on which you can upload the actual file data.

See the python example as a guide to how to use this call.

We highly suggest that you use HTTPS when using these API calls. Using HTTP is unsafe and can expose your data to unwanted parties.

Feel free to create code in other languages and for other environments based on the above specifications. To submit your code for the comunnity to use, just create a pull-request and we would be happy to include your code here.
