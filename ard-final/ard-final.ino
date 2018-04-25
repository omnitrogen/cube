// Arduino serial communication with Raspi
/*
String inData;
const int spr = 200 * 32 ;

void setup() {
    Serial.begin(9600);
    for (int i=0 ; i<10 ; i++){
        pinMode(i, OUTPUT);
        digitalWrite(i,LOW);
    }
    
    
    
    pinMode(10,OUTPUT);
    digitalWrite(10,HIGH);
    
    pinMode(11,OUTPUT);
    digitalWrite(11,LOW);
    
    pinMode(12,OUTPUT);
    digitalWrite(12,HIGH);
}

void loop() {
    if (Serial.available()) {

        inData = Serial.readString();

        for (int i = 0; i < inData.length(); i++) {
            switch (inData[i]) {

            case 'a':
                turn(1, 0, 1, 0, 0.25);
                //Serial.print("OK");
                break;

            case 'b':
                turn(1, 0, 1, 0, 0.5);
                //Serial.print("OK");
                break;

            case 'c':
                turn(1, 1, 1, 0, 0.25);
                //Serial.print("OK");
                break;

            case 'd':
                turn(2, 0, 3, 2, 0.25);
                //Serial.print("OK");
                break;

            case 'e':
                turn(2, 0, 3, 2, 0.5);
                //Serial.print("OK");
                break;

            case 'f':
                turn(2, 1, 3, 2, 0.25);
                //Serial.print("OK");
                break;

            case 'g':
                turn(3, 0, 5, 4, 0.25);
                //Serial.print("OK");
                break;

            case 'h':
                turn(3, 0, 5, 4, 0.5);
                //Serial.print("OK");
                break;

            case 'i':
                turn(3, 1, 5, 4, 0.25);
                Serial.print("OK");
                break;

            case 'j':
                turn(4, 0, 7, 6, 0.25);
                //Serial.print("OK");
                break;

            case 'k':
                turn(4, 0, 7, 6, 0.5);
                //Serial.print("OK");
                break;

            case 'l':
                turn(4, 1, 7, 6, 0.25);
                //Serial.print("OK");
                break;

            case 'm':
                turn(5, 0, 9, 8, 0.25);
                //Serial.print("OK");
                break;

            case 'n':
                turn(5, 0, 9, 8, 0.5);
                //Serial.print("OK");
                break;

            case 'o':
                turn(5, 1, 9, 8, 0.25);
                //Serial.print("OK");
                break;

            case 'z':
                Serial.write("DN");
                delay(1000);
                break;

            }
            Serial.write(inData[i]);
        }

    }
}

void turn(int numMoteur, int sens, int pinPas, int pinSens, float rot) {
    
    digitalWrite(pinSens, sens);
    
    for(int k = 0; k <= spr * rot; k++){
        digitalWrite(pinPas, HIGH);
        delayMicroseconds(500);
        digitalWrite(pinPas, LOW);
        delayMicroseconds(500);
    }
}
*/



String inData;
const int spr = 200;

void setup() {
    Serial.begin(9600);
    
    pinMode(2, OUTPUT);
    digitalWrite(2,LOW);
    
    pinMode(4, OUTPUT);
    digitalWrite(4,LOW);

    
    pinMode(8,OUTPUT);
    digitalWrite(16,HIGH);
    
    pinMode(12,OUTPUT);
    digitalWrite(10,HIGH);
    delay(1000);
    Serial.print("init ok");

}

void loop() {

    if (Serial.available()) {

        inData = Serial.readString();

        for (int i = 0; i < inData.length(); i++) {
            switch (inData[i]) {

            case 'a':
                turn(1, 0, 1, 0, 0.25);
                //Serial.print("OK");
                break;

            case 'b':
                turn(1, 0, 1, 0, 0.5);
                //Serial.print("OK");
                break;

            case 'c':
                turn(1, 1, 1, 0, 0.25);
                //Serial.print("OK");
                break;

            case 'd':
                turn(2, 0, 3, 2, 0.25);
                //Serial.print("OK");
                break;

            case 'e':
                turn(2, 0, 3, 2, 0.5);
                //Serial.print("OK");
                break;

            case 'f':
                turn(2, 1, 3, 2, 0.25);
                //Serial.print("OK");
                break;

            case 'g':
                turn(3, 0, 5, 4, 0.25);
                //Serial.print("OK");
                break;

            case 'h':
                turn(3, 0, 5, 4, 0.5);
                //Serial.print("OK");
                break;

            case 'i':
                turn(3, 1, 5, 4, 0.25);
                Serial.print("OK");
                break;

            case 'j':
                turn(4, 0, 7, 6, 0.25);
                //Serial.print("OK");
                break;

            case 'k':
                turn(4, 0, 7, 6, 0.5);
                //Serial.print("OK");
                break;

            case 'l':
                turn(4, 1, 7, 6, 0.25);
                //Serial.print("OK");
                break;

            case 'm':
                turn(5, 0, 9, 8, 0.25);
                //Serial.print("OK");
                break;

            case 'n':
                turn(5, 0, 9, 8, 0.5);
                //Serial.print("OK");
                break;

            case 'o':
                turn(5, 1, 9, 8, 0.25);
                //Serial.print("OK");
                break;
                
                
            case 'p':
                turn(5, 0, 4, 2, 0.25);
                //Serial.print("OK");
                break;
                
            case 'q':
                turn(5, 0, 4, 2, 0.5);
                //Serial.print("OK");
                break;

            case 'r':
                turn(5, 1, 4, 2, 0.25);
                //Serial.print("OK");
                break;



            case 'z':
                Serial.write("DN");
                delay(1000);
                break;

            }
            Serial.write(inData[i]);
        }

    }
}

void turn(int numMoteur, int sens, int pinPas, int pinSens, float rot) {
    
    digitalWrite(pinSens, sens);
    
    for(int k = 0; k < spr * rot; k++){
        digitalWrite(pinPas, HIGH);
        delayMicroseconds(1000);
        digitalWrite(pinPas, LOW);
        delayMicroseconds(1000);
    }
}
