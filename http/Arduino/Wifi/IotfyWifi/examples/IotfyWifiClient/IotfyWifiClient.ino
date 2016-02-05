/*
//Keep extra care for sending the JSON, because it interprets special characters, so use escape char along.
*/

#include <IotfyWifi.h>
#include <WiFi.h>
#include <SPI.h>

IotfyWifiClass IotfyWifi(DEBUG_ON);  


char ssid[] = "MY_SSID"; //  your network SSID (name)
char pass[] = "MY_PASS";    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number s(needed only for WEP)

String X_ID="XXXXXX";
String X_CLIENT="XXXXXX";


void setup()
{
 
Serial.begin(9600);
int x=IotfyWifi.init();
int status = WL_IDLE_STATUS;
while (status != WL_CONNECTED)
	{
		Serial.print("Attempting to connect to SSID: ");
		Serial.println(ssid);
		// Connect to WPA/WPA2 network. Change this line if using open or WEP network:
		status = WiFi.begin(ssid, pass);
	}
if (x==0)
  {
    Serial.println("Wifi configured");
    IotfyWifi.printWifiStatus();
    IotfyWifi.set_id(X_ID,X_CLIENT);
  }

}

void loop()
{
   for(int i=0;i<1024;i++)
  {
   IotfyWifi.postdata("DemoSensors","TEST001","GPIO1",(String)i);
   IotfyWifi.getdata(800,4);
   Serial.println("outa getdata");
  }
}
