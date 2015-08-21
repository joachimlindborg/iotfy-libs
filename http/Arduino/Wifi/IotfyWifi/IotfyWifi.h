/*
 *   Iotfy_ethernet.h - Library for Iotfy_Ethernet.
 *     Created by Iotfy, --some data--.
 *       Released into the public domain.
 *       */


#ifndef IotfyWifi_h
#define IotfyWifi_h
#include "Arduino.h"
#include <WiFi.h>
#include <SPI.h>

#ifndef NON_BLOCKING
#define NON_BLOCKING 0
#endif

#ifndef BLOCKING 
#define BLOCKING 1
#endif
#ifndef DEBUG_ON
#define DEBUG_ON 1
#endif

#ifndef DEBUG_OFF 
#define DEBUG_OFF 0
#endif

class IotfyWifiClass
{
	private:
		int _debugflag;
		//int status;
	public:
		String X_IOTFY_ID,X_IOTFY_CLIENT;   
		IotfyWifiClass(int);
		int init();
		void set_id(String, String);
		void postdata(String, String, String, String);
		String getdata(int,int);
		void debug(String);
		int printWifiStatus();
		void disconnect();

};
extern IotfyWifiClass IotfyWifi;
#endif

