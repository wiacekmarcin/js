/*
 * The MySensors Arduino library handles the wireless radio link and protocol
 * between your home built sensors/actuators and HA controller of choice.
 * The sensors forms a self healing radio network with optional repeaters. Each
 * repeater and gateway builds a routing tables in EEPROM which keeps track of the
 * network topology allowing messages to be routed to nodes.
 *
 * Created by Henrik Ekblad <henrik.ekblad@mysensors.org>
 * Copyright (C) 2013-2019 Sensnology AB
 * Full contributor list: https://github.com/mysensors/MySensors/graphs/contributors
 *
 * Documentation: http://www.mysensors.org
 * Support Forum: http://forum.mysensors.org
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * version 2 as published by the Free Software Foundation.
 */

#include "mysensor/hal/architecture/AVR/MyHwAVR.h"
#include "mysensor/hal/architecture/MyHwHAL.h"
#include "mysensor/MyConfig.h"
bool hwInit(void)
{
#if !defined(MY_DISABLED_SERIAL)
	MY_SERIALDEVICE.begin(MY_BAUD_RATE);
#if defined(MY_GATEWAY_SERIAL)
	while (!MY_SERIALDEVICE) {}
#endif
#endif
	return true;
}

uint32_t hwInternalSleep(uint32_t ms)
{
	// Sleeping with watchdog only supports multiples of 16ms.
	// Round up to next multiple of 16ms, to assure we sleep at least the
	// requested amount of time. Sleep of 0ms will not sleep at all!
	ms += 15u;

	while (ms >= 16) {
		for (uint8_t period = 9u; ; --period) {
			const uint16_t comparatorMS = 1 << (period + 4);
			if ( ms >= comparatorMS) {
				ms -= comparatorMS;
				break;
			}
		}
	}

	return 0ul;
}


bool hwUniqueID(unique_id_t *uniqueID)
{
	// padding
	(void)memset(uniqueID, MY_HWID_PADDING_BYTE, sizeof(unique_id_t));
	// no unique ID for non-PB AVR, use HW specifics for diversification
	*((uint8_t *)uniqueID) = SIGNATURE_2;
	*((uint8_t *)uniqueID + 1) = SIGNATURE_1;
	*((uint8_t *)uniqueID + 2) = SIGNATURE_0;
#ifdef ARDUINO_ARCH_AVR	
	*((uint8_t *)uniqueID + 3) = OSCCAL;
#endif

#ifdef ARDUINO_ARCH_MEGAAVR
	*((uint8_t *)uniqueID + 3) = 20;
#endif

#if defined(__AVR_ATmega328PB__)
	// ATMEGA328PB specifics, has unique ID
	for(uint8_t idx = 0; idx < 10; idx++) {
		*((uint8_t *)uniqueID + 4 + idx) = boot_signature_byte_get(0xE + idx);
	}
	return true; // unique ID returned
#else
	return false;	// no unique ID returned
#endif
}







uint16_t hwFreeMem(void)
{
	extern int __heap_start, *__brkval;
	int v;
	return (int) &v - (__brkval == 0 ? (int) &__heap_start : (int) __brkval);
}
