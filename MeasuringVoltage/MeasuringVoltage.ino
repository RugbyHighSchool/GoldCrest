// Measuring Voltage.
const int LEDArray[] = {2,3,4,5,6,7,8,9};
const bool DEBUG = true;

void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT); // pin to measure the voltage
  for(int i = 0; i < sizeof(LEDArray); i++) {
    pinMode(LEDArray[i], OUTPUT);
  }
  if (debug) { 
  Serial.begin(9600);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
//  Serial.println(analogRead(A0));
  int tmp = map(analogRead(A0), 0, 1023, 0, sizeof(LEDArray)/2);
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
  for (int i = 0; i < sizeof(LEDArray); i++) {
    digitalWrite(LEDArray[i], LOW);
  }
}
