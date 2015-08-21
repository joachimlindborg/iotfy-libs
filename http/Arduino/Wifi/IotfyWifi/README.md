/////////////////////////////////////////////////////////////////////
				README 
////////////////////////////////////////////////////////////////////

1.  Initiallise the IotfyClass with only one parameter 
    -- DEBUG_ON/DEBUG_OFF, which is simply a macro

2.  init function takes two arguments
    -- byte array for MAC address
    -- IP adress which is of type IPAddress in Ethernet Library.
    -- returns 0 on success else -1.


3.  set_id function takes two arguments
    -- X_IOTFY_ID 
    -- X_IOTFY_CLIENT
    both of which will be given to you via Web Dashboard on signup

4.  Postdata takes only one argument
    -- String to be sent

5.  Getdata take two argument
    -- first Integer is Number of bytes to read from server
    -- second Integer is Timeout, in case of desired number of bytes are not recieved.
    -- Returns String obtained from server

