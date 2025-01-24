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

#include "mysensor/hal/architecture/MyHwHAL.h"
#include "mysensor/MyConfig.h"
#include "mysensor/core/MyMessage.h"
void hwDebugPrint(const char *fmt, ...)
{
#ifndef MY_DISABLED_SERIAL
#if !defined(__linux__)
	char fmtBuffer[MY_SERIAL_OUTPUT_SIZE];
#ifdef MY_GATEWAY_SERIAL
	// prepend debug message to be handled correctly by controller (C_INTERNAL, I_LOG_MESSAGE)
	snprintf_P(fmtBuffer, sizeof(fmtBuffer), PSTR("0;255;%" PRIu8 ";0;%" PRIu8 ";"), C_INTERNAL,
	           I_LOG_MESSAGE);
#ifdef DEBUGDEVICE	
	MY_DEBUGDEVICE.print(fmtBuffer);
#endif	
#endif
	// prepend timestamp
#ifdef DEBUGDEVICE	
	MY_DEBUGDEVICE.print(fmtBuffer);
	MY_DEBUGDEVICE.print(hwMillis());
	MY_DEBUGDEVICE.print(" ");
#endif	

	
	va_list args;
	va_start(args, fmt);
	vsnprintf_P(fmtBuffer, sizeof(fmtBuffer), fmt, args);
#ifdef MY_GATEWAY_SERIAL
	// Truncate message if this is gateway node
	fmtBuffer[sizeof(fmtBuffer) - 2] = '\n';
	fmtBuffer[sizeof(fmtBuffer) - 1] = '\0';
#endif
	va_end(args);
#ifdef DEBUGDEVICE	
	MY_DEBUGDEVICE.print(fmtBuffer);
	MY_DEBUGDEVICE.flush();
#endif	
#else
	va_list args;
	va_start(args, fmt);
	vlogDebug(fmt, args);
	va_end(args);
#endif
#else
	(void)fmt;
#endif
}

#if defined(DEBUG_OUTPUT_ENABLED)
static char hwDebugPrintStr[65];
static void hwDebugBuf2Str(const uint8_t *buf, size_t sz)
{
	if (sz > 32) {
		sz = 32; //clamp to 32 bytes
	}
	for (uint8_t i = 0; i < sz; i++) {
		hwDebugPrintStr[i * 2] = convertI2H(buf[i] >> 4);
		hwDebugPrintStr[(i * 2) + 1] = convertI2H(buf[i]);
	}
	hwDebugPrintStr[sz * 2] = '\0';
}
#endif
