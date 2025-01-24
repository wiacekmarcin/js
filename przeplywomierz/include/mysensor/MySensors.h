#ifndef MySensorsSG_h
#define MySensorsSG_h

#include <Arduino.h>

#include "mysensor/MyConfig.h"
//#include "mysensor/core/MyHelperFunctions.cpp"
#include "mysensor/core/MySensorsCore.h"

// HARDWARE
#include "mysensor/hal/architecture/MyHwHAL.h"
//#include "mysensor/hal/architecture/AVR/MyHwAVR.cpp"
//#include "mysensor/hal/architecture/MyHwHAL.cpp"

// commonly used macros, sometimes missing in arch definitions
#if !defined(_BV)
#define _BV(x) (1<<(x))	//!< _BV
#endif

#if !defined(min) && !defined(__linux__)
#define min(a,b) ((a)<(b)?(a):(b)) //!< min
#endif

#if !defined(max) && !defined(__linux__)
#define max(a,b) ((a)>(b)?(a):(b)) //!< max
#endif

#if !defined(MIN)
#define MIN min //!< MIN
#endif

#if !defined(MAX)
#define MAX max //!< MAX
#endif



// GATEWAY - SERIAL
//#include "mysensor/core/MyGatewayTransportSerial.cpp"

// PARENT CHECK
#if defined(MY_PARENT_NODE_IS_STATIC) && (MY_PARENT_NODE_ID == AUTO)
#error Parent is static but no parent ID defined, set MY_PARENT_NODE_ID.
#endif

#include "mysensor/core/MyCapabilities.h"
//#include "mysensor/core/MyMessage.cpp"
//#include "mysensor/core/MySensorsCore.cpp"


#endif

/** @}*/
