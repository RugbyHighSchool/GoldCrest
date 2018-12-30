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

void setup() {
  lcd.begin();
}

void loop() {
  // put your main code here, to run repeatedly:

}
