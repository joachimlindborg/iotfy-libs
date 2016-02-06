/*

//Keep extra care for sending the JSON, because it interprets special characters, so use escape char along.
*/



#include <IotfyEthernet.h>
#include <Ethernet.h>
#include <SPI.h>

IotfyClass Iotfy(DEBUG_ON);  
byte mac[]={0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
IPAddress ip(192,168,1,50);

String X_ID="XXXXXX";
String X_CLIENT="XXXXXX";

void setup()
{
 
Serial.begin(9600);
int x=Iotfy.init();
if (Ethernet.begin(mac) == 0) 
  {
    Iotfy.debug("Failed to configure Ethernet using DHCP");
    Iotfy.debug("Now trying static IP");
    Ethernet.begin(mac,ip);
  }
else
    Iotfy.debug("couldn't set Ethernet");

if (x==0)
  {
    Serial.println("Ethernet configured");
    Iotfy.print_ip_address();
    Iotfy.set_id(X_ID,X_CLIENT);
  }

}

void loop()
{
  for(int i=0;i<1024;i++)
  {
   Iotfy.postdata("ArduinoEthernet","Dev01","GPIO1",(String)i);
   Iotfy.getdata(800,4);
   Serial.println("outa getdata");
  }
}
