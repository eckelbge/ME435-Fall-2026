String inputString = "";
bool isStringComplete = false;

void setup() {
  Serial.begin(19200);
  inputString.reserve(200);
  pinMode(13,OUTPUT);
}

void loop() {
  if (isStringComplete) {
    if(inputString.equals("LED ON")){
      digitalWrite(13,HIGH);
      Serial.println("LED On");
    } else if(inputString.equals("LED OFF")){
      digitalWrite(13,LOW);
      Serial.println("LED Off");
    } else if(inputString.equals("FLASH 3 1000")){
      int flashnum = 3;
      int flashwait = 1000;
      for (int i=0; i<=flashnum; i++){
        digitalWrite(13,HIGH);
        delay(flashwait/2);
        digitalWrite(13,LOW);
        delay(flashwait/2);
      }
      digitalWrite(13,LOW);
      Serial.println("Flashes = 3 PeriodMs = 1000");
    } else{
      Serial.print("Unknown command -->");
      Serial.println(inputString);
    }

    inputString = "";
    isStringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      isStringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}
