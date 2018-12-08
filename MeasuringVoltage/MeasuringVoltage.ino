// Measuring Voltage.
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const int LEDArray[] = {2, 3, 4, 5, 6, 7, 8, 9};
const bool debug = true;

LiquidCrystal_I2C lcd(0x27, 16, 2);


void setup() {
  pinMode(A0, INPUT); // pin to measure the voltage
  for (int i = 0; i < sizeof(LEDArray); i++) {
    pinMode(LEDArray[i], OUTPUT);
  }
  if (debug) {
    Serial.begin(9600);
  }

  lcd.begin();
  lcd.print("RHS Gold Crest");
}

void loop() {
  int tmp = map(analogRead(A0), 0, 1020, 0, sizeof(LEDArray) / 2); // convert analogRead from 0-1023 to the number of LEDs we have.
  if (debug) {
    Serial.print("Analog Value: ");
    Serial.print(analogRead(A0));
    Serial.print(" Temp Value: ");
    Serial.println(tmp);
  }
  lcd.setCursor(0,1);
  lcd.print("Voltage: ");
  lcd.print(analogRead(A0));

  for (int j = 0; j < tmp; j++) {
    digitalWrite(LEDArray[j], HIGH);
  }
  delay(100);
  for (int i = 0; i < sizeof(LEDArray)/2; i++) {
    digitalWrite(LEDArray[i], LOW);
  }
  delay(100);
}
