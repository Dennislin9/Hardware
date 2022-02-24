
int status[] = {LOW, HIGH};
int signalState = LOW;
int signal2State = LOW;


void setup() {
  // put your setup code here, to run once:
  pinMode(9, INPUT);

  pinMode(8, OUTPUT);
}

void loop() {

  if(signal2State) signal2State = digitalRead(9);
  if(digitalRead(9) != signal2State) {
    signalState = (signalState == LOW) ? HIGH : LOW;
    digitalWrite(8, signalState);
    signal2State = HIGH;
  }
}
