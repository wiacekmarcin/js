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

#include "mysensor/MyConfig.h"
#include "mysensor/core/MyProtocol.h"
#include "mysensor/core/MyHelperFunctions.h"
#include <string.h>

char _fmtBuffer[MY_GATEWAY_MAX_SEND_LENGTH];
char _convBuffer[MAX_PAYLOAD_SIZE * 2 + 1];

bool protocolSerial2MyMessage(MyMessage &message, char *inputString)
{
	char *str, *p;
	uint8_t index = 0;
	mysensors_command_t command = C_INVALID_7;
	message.setSender(GATEWAY_ADDRESS);
	message.setLast(GATEWAY_ADDRESS);
	message.setEcho(false);

	// Extract command data coming on serial line
	for (str = strtok_r(inputString, ";", &p); // split using semicolon
	        str && index < 5; // loop while str is not null an max 4 times
	        str = strtok_r(NULL, ";", &p), index++ // get subsequent tokens
	    ) {
		switch (index) {
		case 0: // Radio id (destination)
			message.setDestination(atoi(str));
			break;
		case 1: // Child id
			message.setSensor(atoi(str));
			break;
		case 2: // Message type
			command = static_cast<mysensors_command_t>(atoi(str));
			message.setCommand(command);
			break;
		case 3: // Should we request echo from destination?
			message.setRequestEcho(atoi(str) ? 1 : 0);
			break;
		case 4: // Data type
			message.setType(atoi(str));
			break;
		}
	}
	// payload
	if (str == NULL) {
		// no payload, set default value
		message.set((uint8_t)0);
	} else if (command == C_STREAM) {
		// stream payload
		uint8_t bvalue[MAX_PAYLOAD_SIZE];
		uint8_t blen = 0;
		while (*str) {
			uint8_t val;
			val = convertH2I(*str++) << 4;
			val += convertH2I(*str++);
			bvalue[blen] = val;
			blen++;
		}
		message.set(bvalue, blen);
	} else {
		// regular payload
		char *value = str;
		// Remove trailing carriage return and newline character (if it exists)
		const uint8_t lastCharacter = strlen(value) - 1;
		if (value[lastCharacter] == '\r' || value[lastCharacter] == '\n') {
			value[lastCharacter] = '\0';
		}
		message.set(value);
	}
	return (index == 5);
}

char *protocolMyMessage2Serial(MyMessage &message)
{
	(void)snprintf_P(_fmtBuffer, (uint8_t)MY_GATEWAY_MAX_SEND_LENGTH,
	                 PSTR("%" PRIu8 ";%" PRIu8 ";%" PRIu8 ";%" PRIu8 ";%" PRIu8 ";%s\n"), message.getSender(),
	                 message.getSensor(), message.getCommand(), message.isEcho(), message.getType(),
	                 message.getString(_convBuffer));
	return _fmtBuffer;
}

