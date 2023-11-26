#ifndef _LCD_H_
#define _LCD_H_
#include <Arduino.h>
#define ISLCD  8
//#define LCD_DEBUG 


#ifdef LCD_DEBUG
void lcd_init();
void lcd_connect();
void lcd_print(uint8_t inD); 
#endif
#endif