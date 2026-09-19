#include "lcd.h"

#include "Arduino.h"

#ifdef LCD_DEBUG
#include <LiquidCrystal_I2C.h>
// set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x3F,16,4); 
bool connectLcd = false;
void lcd_init()
{
    pinMode(ISLCD, INPUT);
    lcd.init();     
    lcd.clear();
 
    // Print a message to the LCD.
    lcd.backlight();
    lcd.print("0 1 2 3 4 5 6 7");
    connectLcd = true;
}

void lcd_connect() {
    
    if (digitalRead(ISLCD) == LOW && !connectLcd) {
        connectLcd = true;
        lcd.init();     
        lcd.clear();
        lcd.print("0 1 2 3 4 5 6 7");
        lcd.backlight();
    } else {
        connectLcd = false;
    }
}

void lcd_print(uint8_t inD) 
{
    lcd_connect();
    if (connectLcd) {
        lcd.setCursor(0,1);
        lcd.print(MASK(inD, 0)?'1':'0');
        lcd.print(' ');
        lcd.print(MASK(inD, 1)?'1':'0');
        lcd.print(' ');
        lcd.print(MASK(inD, 2)?'1':'0');
        lcd.print(' ');
        lcd.print(MASK(inD, 3)?'1':'0');
        lcd.print(' ');
        lcd.print(MASK(inD, 4)?'1':'0');
        lcd.print(' ');
        lcd.print(MASK(inD, 5)?'1':'0');
        lcd.print(' ');
        lcd.print(MASK(inD, 6)?'1':'0');
        lcd.print(' ');
        lcd.print(MASK(inD, 7)?'1':'0');
        lcd.cursor_off();
    }
}
#endif