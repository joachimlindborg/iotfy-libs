
#include "Arduino.h"
#include "IotfyEthernet.h"

EthernetClient client;

int IotfyClass::init()
{
	debug("Init being called");
	return 0;
}


IotfyClass::IotfyClass(int debug_val)
{
	_debugflag=debug_val;
}

void IotfyClass::debug(String data)
{
	if(_debugflag)
	{
		Serial.println(data);
	}
}

void IotfyClass::set_id(String IOTFY_ID, String IOTFY_CLIENT)
{
	debug("set id being called");
	X_IOTFY_ID="X-IOTFY-ID: "+IOTFY_ID;
	X_IOTFY_CLIENT="X-IOTFY-CLIENT: "+IOTFY_CLIENT;
	debug(X_IOTFY_CLIENT);	
	debug(X_IOTFY_ID);
	debug("exiting set_id");
}
  

void IotfyClass::print_ip_address()
{
	for (byte thisByte = 0; thisByte < 4; thisByte++) 
	 {
	    Serial.print(Ethernet.localIP()[thisByte], DEC);
	    Serial.print("."); 
	 }
	 Serial.println();
}  


void IotfyClass::postdata(String group_iotfy, String id_iotfy, String tag_iotfy, String value_iotfy)
{
debug("in postdata");
char *server="www.iotfy-ws.appspot.com";
String data="\{\"group\":\"";
data+=group_iotfy;
data+="\", \"device\":\"";
data+=id_iotfy;
data+="\", \"data\":\"";
data+="\[\{\"tag\":\"";
data+=tag_iotfy;
data+="\",\"text\":\"";
data+=value_iotfy;
data+="\"]\}\"";

while(1)
{
	debug("Trying to connect");
	if (client.connect(server, 80))
	{
		debug("connected and now sending post request");
		client.println("POST /api/telemetry/v1/post_text_data HTTP/1.0");
		client.println("User-Agent: arduino-ethernet");
		client.println("Host: www.iotfy-ws.appspot.com");
		//client.println("X-IOTFY-ID: 5715999101812736");
		//client.println("X-IOTFY-CLIENT: 49028b37-ab1b-4690-a315-4f0b64f6e5e0");
		client.println(X_IOTFY_ID);
		client.println(X_IOTFY_CLIENT);	
		client.println("Content-Type: application/json");
		client.print("Content-Length: ");
		client.println(data.length()); 
		client.println();
		client.println(data); 
		client.println("Connection: close");


		if(_debugflag)
		{ 
		debug("connected");
		debug("POST /d/send_txt_data HTTP/1.1");
		debug("User-Agent: arduino-ethernet");
		debug("Host: www.iotfy-ws.appspot.com");
		debug(X_IOTFY_ID);
		debug(X_IOTFY_CLIENT);
		debug("Content-Type: application/json");
		debug("Content-Length: ");
		debug((String)data.length()); 
		debug("");
		debug(data); 
		}
		break;
	}
}
}

String IotfyClass::getdata(int no_of_bytes, int timeout)
{
int ctr=0;
int pt=millis()/1000;
String data="";
data.reserve(no_of_bytes);
while(1)
{
	if(client.available())
	{
		char c=client.read();
		data+=c;
		Serial.print(c);
		ctr++;
		if(ctr==no_of_bytes)
			break;
	}      
	else
	{
		if(millis()/1000-pt>timeout)
		{
			pt=millis()/1000;
			break;		
		}	
	}
}
disconnect();
return data;
}


void IotfyClass::disconnect()
{
	debug("disconnecting..");
	client.flush();
	client.stop();
}

