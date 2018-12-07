// Measuring Voltage.
const int LEDArray[] = {2,3,4,5,6,7,8,9};

void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT); // pin to measure the voltage
  for(int i = 0; i < sizeof(LEDArray); i++) {
    pinMode(LEDArray[i], OUTPUT);
  }
  
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int j=0; j < sizeof(LEDArray); j++) {
    digitalWrite(LEDArray[j], HIGH);
    delay(500);
  }

  delay(2000);

  for(int k=0; k < sizeof(LEDArray); k++) {
    digitalWrite(LEDArray[k], LOW);
    delay(500);
  }
}
 
