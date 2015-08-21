/*
 *   Iotfy_ethernet.h - Library for Iotfy_Ethernet.
 *     Created by Iotfy, --some data--.
 *       Released into the public domain.
 *       */


#ifndef Iotfy_h
#define Iotfy_h
#include "Arduino.h"
#include <Ethernet.h>
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

class IotfyClass
{
	private:
		int _debugflag;
	public:
		String X_IOTFY_ID,X_IOTFY_CLIENT;   
		IotfyClass(int);
		int init();
		void set_id(String, String);
		void print_ip_address();
		void postdata(String, String, String, String);
		String getdata(int,int);
		void debug(String);
		void disconnect();

};
extern IotfyClass Iotfy;
#endif

