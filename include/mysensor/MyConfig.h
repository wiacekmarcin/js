/*
 * The MySensors Arduino library handles the wireless radio link and protocol
 * between your home built sensors/actuators and HA controller of choice.
 * The sensors forms a self healing radio network with optional repeaters. Each
 * repeater and gateway builds a routing tables in RAM or EEPROM which keeps track of the
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
 * @file MyConfig.h
 * @ingroup MyConfigGrp
 * @brief MySensors specific configuration flags.
 * @{
 * Set these in your sketch before including MySensors.h to customize the library to your needs.
 * If the sketch does not define these flags, they will get default values where applicable.
 */
#ifndef MyConfig_h
#define MyConfig_h

/**
 * @defgroup SerialDebugGrpPub Serial and debugging
 * @ingroup MyConfigGrp
 * @brief These options control serial and debugging features and functionalities in the library.
 * @{
 */

/**
 * @def MY_DEBUG
 * @brief Define MY_DEBUG to show debug prints.
 *
 * This option will add a lot to the size of the final sketch but is helpful to see what is actually
 * is happening during development.
 *
 * @note Values in parenthesis indicate default values which will be used if you have not defined
 * the flag in your sketch.
 */
//#define MY_DEBUG

/**
 * @def MY_DEBUGDEVICE
 * @brief Define MY_DEBUGDEVICE to redirect debug prints.
 *
 * If defined, MY_DEBUGDEVICE replaces MY_SERIALDEVICE for the purpose
 * of printing debug messages.  This only applies to debugging.
 *
 * The intent is to provide the ability to send debugging messages
 * out a different serial port than what is being used for
 * communication between nodes or from gateway to controller when
 * this communication uses a serial interface.  This assumes that
 * the MY_DEBUGDEVICE serial interface already exists. It can be a
 * hardware serial device or a software serial device.
 */
//#define MY_DEBUGDEVICE

#define MY_SERIALDEVICE Serial

/**
 * @def MY_BAUD_RATE
 * @brief Serial output baud rate (debug prints and serial gateway speed).
 *
 * The baud rate configured here must match the baud rate at the "other" end.
 *
 * @warning Depending on your target device and clock speed, certain baud rates might not work well.
 */
#ifndef MY_BAUD_RATE
#define MY_BAUD_RATE (115200ul)
#endif

/**
 * @def MY_SERIAL_OUTPUT_SIZE
 * @brief Maximum characters for serial output.
 *
 * If you are running extremely low on memory, reducing this size might just save your day.
 */
#ifndef MY_SERIAL_OUTPUT_SIZE
#define MY_SERIAL_OUTPUT_SIZE (120u)
#endif
/** @}*/ // End of SerialDebugGrpPub group


/**
 * @defgroup GatewaySettingGrpPub Gateway
 * @ingroup MyConfigGrp
 * @brief These options control gateway specific configurations.
 * @{
 */
/**
 * @def MY_GATEWAY_MAX_RECEIVE_LENGTH
 * @brief Max buffersize needed for messages coming from controller.
 */
#ifndef MY_GATEWAY_MAX_RECEIVE_LENGTH
#define MY_GATEWAY_MAX_RECEIVE_LENGTH (100u)
#endif

/**
 * @def MY_GATEWAY_MAX_SEND_LENGTH
 * @brief Max buffer size when sending messages.
 */
#ifndef MY_GATEWAY_MAX_SEND_LENGTH
#define MY_GATEWAY_MAX_SEND_LENGTH (120u)
#endif

/**
 * @def MY_GATEWAY_MAX_CLIENTS
 * @brief Max number of parallel clients (sever mode).
 */
#ifndef MY_GATEWAY_MAX_CLIENTS
#define MY_GATEWAY_MAX_CLIENTS (1u)
#endif

#define MY_GATEWAY_SERIAL

/**
 * @defgroup LinuxSettingGrpPub Linux
 * @ingroup PlatformSettingGrpPub
 * @brief These options control Linux specific configurations.
 * @{
 */


/*
* "Helper" definitions
*/

/*
 * Detect node type
 * MY_GATEWAY_FEATURE is set for gateway sketches.
 * MY_IS_GATEWAY is true when @ref MY_GATEWAY_FEATURE is set.
 * MY_NODE_TYPE contain a string describing the class of sketch/node (gateway/repeater/node).
 */
#if defined(MY_GATEWAY_SERIAL)
#define MY_GATEWAY_FEATURE
#define MY_IS_GATEWAY (true)
#define MY_NODE_TYPE "GW"
#endif



#define DEBUG_OUTPUT(x,...)								//!< debug NULL


#endif	// MyConfig_h


/** @}*/ // End of MyConfig group
