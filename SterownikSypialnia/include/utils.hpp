#ifndef _UTILS_H_
#define _UTILS_H_

#include <Arduino.h>
#include "decl_io.hpp"

#ifdef DEBUG_CODE
void print_64val(uint64_t value);
void print_64val1(uint64_t value);

void print_64bin(uint64_t value, bool input);

void print_64Out(uint64_t value);

void mcp_print(short ps);
#endif

void print1_64bin(uint64_t value);
void print1_64val(uint64_t value);

void mcp_pinMode(short ps);

void mcp_digitalWrite(short ps, short value);

bool isOutput(short ps);

void mcp_pinAttactInterrupt(short ps);

short mcp_getPinMode(short ps);

#endif
