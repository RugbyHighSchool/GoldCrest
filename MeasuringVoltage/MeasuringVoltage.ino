// Measuring Voltage.
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const int LEDArray[] = {2, 3, 4, 5, 6, 7, 8, 9};
const bool debug = true;

int currentValue = 0;
int previousValue = 0;

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
  lcd.setCursor(0,1);
}

void loop() {
  currentValue = map(analogRead(A0), 0, 1020, 0, sizeof(LEDArray) / 2);
 
  if (currentValue != previousValue) {
    if (currentValue < previousValue) {
      for (int i = 0; i < sizeof(LEDArray) / 2; i++) {
        digitalWrite(LEDArray[i], LOW);
      }
    }
    lcd.print("Voltage: ");
    lcd.print(currentValue);
    lcd.print("mV");
    for (int j = 0; j < currentValue; j++) {
      digitalWrite(LEDArray[j], HIGH);
    }

  }

  previousValue = currentValue;

  if (debug) {
    Serial.print(currentValue);
    Serial.print(" : ");
    Serial.println(previousValue);
  }
}
