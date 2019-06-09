int getValue = 0;
int lightInput = 220; // value of when light is on
int lightState = 0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    //String time = String(millis()/1000, DEC);
    String sensorValue = String(analogRead(A0), DEC);
    getValue = analogRead(A0);
    String ledState = String(lightState);
    String finalValue = sensorValue+":"+ledState;
    Serial.println(finalValue);
    delay(1000);
    
    if (getValue < lightInput)
    { 
      digitalWrite(13, HIGH);//LED on
      lightState = 1;
    } 
    else 
    { 
      digitalWrite(13, LOW);// LED off 
      lightState = 0;
    }
}
