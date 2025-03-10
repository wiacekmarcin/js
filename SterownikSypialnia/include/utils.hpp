#ifndef _UTILS_H_
#define _UTILS_H_

#include <Arduino.h>

void print_64val(uint64_t value);

void print_64bin(uint64_t value, bool input);

void print_64Out(uint64_t value);

void mcp_pinMode(short ps);

void mcp_digitalWrite(short ps, short value);

bool isOutput(short ps);

void mcp_pinAttactInterrupt(short ps);

void mcp_print(short ps);

short mcp_getPinMode(short ps);

#endif
