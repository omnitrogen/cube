
byte inData;

void setup(){
  Serial.begin(9600);
  Serial.print("GO");
}

void loop(){
  while (Serial.available() > 0) {
    
    inData = byte(Serial.read());
    // Serial.write(inData);

    /*
    if(inData == 'a'){
      Serial.print("c'est un a");
    }
    
    else if(inData == '1'){
      Serial.print("c'est un 1");
    }
    
    else{
      Serial.print("OVNI");
    }
    */
    
    delay(4000);
    Serial.print(inData);
  }
}
