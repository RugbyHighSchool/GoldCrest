#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int appliancePins[] = {2,3,4,5,6,7,8,9};
// washing machine, fridge, tumbledryer, stove
const int eF = 2;
const int eWM = 3;
const int eTD = 4;
const int eS = 5;

const int bF = 6;
const int bWM = 7;
const int bTD = 8;
const int bS = 9;


void setup() {
  // put your setup code here, to run once:
  lcd.begin();
  lcd.print("Init Boot");  
  for(int i = 0; i < sizeof(appliancePins); i++) {
    pinMode(appliancePins[i], OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  logic("00:00");
  digitalWrite(eF, HIGH);
  digitalWrite(bF, HIGH);
  logic("00:30");
  logic("01:00");
  digitalWrite(eTD, HIGH);
  logic("01:30");
  logic("02:00");
  logic("02:30");
  logic("03:00");
  digitalWrite(eTD, LOW);
  digitalWrite(eS, HIGH);
  logic("03:30");
  logic("04:00");
  logic("04:30");
  logic("05:00");
  digitalWrite(eS, LOW);
  logic("05:30");
  logic("06:00");
  logic("06:30");
  digitalWrite(bS, HIGH);
  digitalWrite(eS, HIGH);
  logic("07:00");
  digitalWrite(eS, LOW);  
  logic("07:30");
  logic("08:00");
  digitalWrite(bS, LOW);
  logic("08:30");
  logic("09:00");
  logic("09:30");
  logic("10:00");
  digitalWrite(eWM, HIGH);
  logic("10:30");
  logic("11:00");
  digitalWrite(eTD, HIGH);
  logic("11:30");
  logic("12:00");
  digitalWrite(eWM, LOW);
  logic("12:30");
  logic("13:00");
  digitalWrite(eTD, LOW);
  logic("13:30");
  logic("14:00");
  logic("14:30");
  logic("15:00");
  logic("15:30");
  logic("16:00");
  logic("16:30");
  logic("17:00");
  digitalWrite(bWM, HIGH);
  logic("17:30");
  logic("18:00");
  digitalWrite(eS, HIGH);
  digitalWrite(bWM, LOW);
  logic("18:30");
  logic("19:00");
  digitalWrite(eS, LOW);
  logic("19:30");
  digitalWrite(bTD, HIGH);
  digitalWrite(bS, HIGH);
  logic("20:00");
  logic("20:30");
  logic("21:00");
  logic("21:30");
  digitalWrite(bTD, LOW);
  digitalWrite(bS, LOW);
  logic("22:00");
  logic("22:30");
  digitalWrite(eWM, HIGH);
  logic("23:00");
  logic("23:30");
  digitalWrite(eWM, LOW);

}

void logic(String dateTime) {
  delay(1000);
  lcd.clear();
  lcd.print("RHS-ElectroRoute");
  lcd.setCursor(0,1);
  lcd.print("Time: ");
  lcd.print(dateTime);
}
