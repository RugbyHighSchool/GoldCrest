
// ApplianceControl
// Written to be used on an Arduino Mega.

// Libraries
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Constants
LiquidCrystal_I2C lcd(0x27, 16, 4); // initalise a 16 by 4 LCD

// Appliances
// g = Good; b = Bad (Inefficient side of the house)
// f = fridge; tv = tv; dw = dishwasher; wm = washing machine; wh = water heater;
const int bF = 2;
const int bTV = 3;
const int bDW = 4;
const int bWM = 5;
const int bWH = 6;
const int gF = 12;
const int gTV = 13;
const int gDW = 14;
const int gWM = 15;
const int gWH = 16;

const int * appliances[] = {&bF, &bTV, &bDW, &bWM, &bWH, &gF, &gTV, &gDW, &gWM, &gWH};

// Electricity Price from the 07062017 in half hour intervals.
const int[] electrictyPrice = {
  2,1.5,-1.11,-1.11,-1.43,-1.43,1.69,2.53,5,9.5,25.14,27,35,38.52,44,44.49,39,38.28,34.11,34,34.5,34.5,36,35.82,35,35,35.12,34.42,29.99,29.8,36,40.62,39.64,39.89,48,48,50.8,50.65,52.5,52.65,56.5,55,50,47,46,44.5,34.79,32.79
}

const int[] electricityUsage = {


}

void setup() {
  lcd.begin();

  for(int i = 0; i < sizeof(appliances); i++) {
    pinMode(appliances[i], OUTPUT); // turns the pin to output.
    digitalWrite(appliances[i], LOW); // turns the led off
  }
}

void loop() {
  // put your main code here, to run repeatedly:


}

void controller(int input, bool good) {
  if (good) {
    if (input == 1) {
      digitalWrite(gF, HIGH);
    } else if(input == 2) {
      digitalWrite(gTV, HIGH);
    }
  }
}
