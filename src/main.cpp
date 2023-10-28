#include <Arduino.h>

// put function declarations here:

unsigned long impulse[2][15];
unsigned short index = 0;

static void WCUmywalkaZ()
{
  impulse[index][0] += 1;
}

static void WCUmywalkaC()
{
  impulse[index][1] += 1;
}

struct PinInterr {
  short pin;
  void (*fun)();
};

PinInterr mapsPin[2] = {
  { 17, WCUmywalkaZ},
  { 16, WCUmywalkaC}
};


void setup() {
  for (int i = 0; i < 2; ++i) {
    for (int j = 0; j < 15; ++j) {
      impulse[i][j] = 0;
    }
  }
  for (int i = 0; i < 2; ++i)
    attachInterrupt(digitalPinToInterrupt(mapsPin[i].pin), mapsPin[i].fun, RISING); 
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:

  delay(1000);
  unsigned short actIndex = index;
  index = (index + 1) % 2;
  for (int j = 0; j < 2; ++j) {
    Serial.print(j, DEC);
    Serial.print(" => ");
    Serial.println(impulse[actIndex][j], DEC);
    impulse[actIndex][j] = 0;
  }
  Serial.println('---');
}

