// Measuring Voltage.
const int LEDArray[] = {2, 3, 4, 5, 6, 7, 8, 9};
const bool debug = true;

void setup() {
  pinMode(A0, INPUT); // pin to measure the voltage
  for (int i = 0; i < sizeof(LEDArray); i++) {
    pinMode(LEDArray[i], OUTPUT);
  }
  if (debug) {
    Serial.begin(9600);
  }
}

void loop() {
  int tmp = map(analogRead(A0), 0, 1020, 0, sizeof(LEDArray) / 2); // convert analogRead from 0-1023 to the number of LEDs we have.
  if (debug) {
    Serial.print("Analog Value: ");
    Serial.print(analogRead(A0));
    Serial.print(" Temp Value: ");
    Serial.println(tmp);
  }

  for (int j = 0; j < tmp; j++) {
    digitalWrite(LEDArray[j], HIGH);
  }
  delay(100);
  for (int i = 0; i < sizeof(LEDArray)/2; i++) {
    digitalWrite(LEDArray[i], LOW);
  }
}
