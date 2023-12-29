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
/**
 * @file MyCapabilities.h
 * @ingroup MyCapabilities
 */

#ifndef MyCapabilities_h
#define MyCapabilities_h
/**
 * @defgroup MyCapabilities Node capabilities indicator
 * @ingroup MyConfigGrp
 *
 * @brief MySensors capabilities indications.
 *
 * At node startup, a capabilities string is shown as part of the initialization logs.
 * This string indicate what configuration the node is running with.
 *
 * The string symbols are ordered in the following way:
 * | Setting   |       Reset       |       Radio       |         OTA        |       Node       |   Architecture   |      Signing     |     Buffering     |   Encryption
 * |-----------|-------------------|-------------------|--------------------|------------------|------------------|------------------|-------------------|-----------------
 * | Indicator | @ref MY_CAP_RESET | @ref MY_CAP_RADIO | @ref MY_CAP_OTA_FW | @ref MY_CAP_TYPE | @ref MY_CAP_ARCH | @ref MY_CAP_SIGN | @ref MY_CAP_RXBUF | @ref MY_CAP_ENCR
 *
 * @see MY_CAPABILITIES
 *
 * @{
 */

// Remote reset
/**
 * @def MY_CAP_RESET
 * @brief Indicate the remote reset setting.
 *
 * @see MY_DISABLE_REMOTE_RESET
 *
 * | Setting    | Indicator
 * |------------|----------
 * | Enabled    | R
 * | Disabled   | N
 */
#if defined(MY_DISABLE_REMOTE_RESET)
#define MY_CAP_RESET "N"
#else
#define MY_CAP_RESET "R"
#endif

// OTA firmware update feature
/**
 * @def MY_CAP_OTA_FW
 * @brief Indicate the OTA update setting.
 *
 * @see MY_OTA_FIRMWARE_FEATURE
 *
 * | Setting    | Indicator
 * |------------|----------
 * | Enabled    | O
 * | Disabled   | N
 */
#if defined(MY_OTA_FIRMWARE_FEATURE)
#define MY_CAP_OTA_FW "O"
#else
#define MY_CAP_OTA_FW "N"
#endif



// Node type
/**
 * @def MY_CAP_TYPE
 * @brief Indicate the type of node.
 *
 * @see MY_GATEWAY_FEATURE, MY_REPEATER_FEATURE, MY_PASSIVE_NODE
 *
 * | Node type | Indicator
 * |-----------|----------
 * | Gateway   | G
 * | Node      | N
 */
#if defined(MY_GATEWAY_FEATURE)
#define MY_CAP_TYPE "G"
#else
#define MY_CAP_TYPE "N"
#endif

// Architecture
/**
 * @def MY_CAP_ARCH
 * @brief Indicate the architecture.
 *
 * @see ARDUINO_ARCH_SAMD, ARDUINO_ARCH_NRF5, ARDUINO_ARCH_ESP8266, ARDUINO_ARCH_AVR, ARDUINO_ARCH_STM32F1, TEENSYDUINO
 *
 * | Architecture | Indicator
 * |--------------|----------
 * | AVR          | A
 */

#elif defined(ARDUINO_ARCH_AVR)
#define MY_CAP_ARCH "A"
#else
#define MY_CAP_ARCH "-"
#endif


/**
 * @def MY_CAPABILITIES
 * @brief This is the resulting capabilities string.
 *
 * @see MY_CAP_RESET, MY_CAP_RADIO, MY_CAP_OTA_FW, MY_CAP_TYPE, MY_CAP_ARCH, MY_CAP_SIGN, MY_CAP_RXBUF, MY_CAP_ENCR
 */
#define MY_CAPABILITIES MY_CAP_RESET MY_CAP_OTA_FW MY_CAP_TYPE MY_CAP_ARCH 

/** @}*/ // End of MyCapabilities group
#endif /* MyCapabilities_h */
