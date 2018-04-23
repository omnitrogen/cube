
byte inData;

void setup(){
  Serial.begin(9600);
  Serial.print("GO");
}

void loop(){
  while (Serial.available() > 0) {
    
    inData = byte(Serial.read());
    // Serial.write(inData);

    if(inData == 'a'){
      Serial.print("OK");
    }
    
    else if(inData == '1'){
      Serial.print("OK");
    }
    
    else{
      Serial.print("NOPE");
    }
  }
}
