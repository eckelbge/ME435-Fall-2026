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
    } else if(inputString.startsWith("FLASH")){
      String args = inputString.substring(6); 
      int spaceIndex = args.indexOf(" "); 
      int numFlashes = args.substring(0, spaceIndex).toInt(); 
      int periodMs = args.substring(spaceIndex + 1).toInt();
      for (int i=1; i<=numFlashes; i++){
        digitalWrite(13,HIGH);
        delay(periodMs/2);
        digitalWrite(13,LOW);
        delay(periodMs/2);
      }
      digitalWrite(13,LOW);
      Serial.print("Flashes = ");
      Serial.print(numFlashes);
      Serial.print(" PeriodMs = ");
      Serial.println(periodMs);
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
