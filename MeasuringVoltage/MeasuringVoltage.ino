// Measuring Voltage.
const int LEDArray[] = {2,3,4,5,6}

void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT); // pin to measure the voltage
  for(int pin : LEDArray) {
    pinMode(pin, OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:

}
