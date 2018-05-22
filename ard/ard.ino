String inData;
const int spr = 200 * 32;

void setup() {
    Serial.begin(9600);

    for (int i=2 ; i<12 ; i++){
        pinMode(i, OUTPUT);
        digitalWrite(i,LOW);
    }

    // maybe add enable PINS ?

    delay(1000);
    // Serial.print("init");
}

void loop() {

    if (Serial.available()) {

        inData = Serial.readString();

        for (int i = 0; i < inData.length(); i++) {
            switch (inData[i]) {

            case 'a':
                turn(0, 3, 2, 0.25);
                break;

            case 'b':
                turn(0, 3, 2, 0.5);
                break;

            case 'c':
                turn(1, 3, 2, 0.25);
                break;

            case 'd':
                turn(0, 5, 4, 0.25);
                break;

            case 'e':
                turn(0, 5, 4, 0.5);
                break;

            case 'f':
                turn(1, 5, 4, 0.25);
                break;

            case 'g':
                turn(0, 7, 6, 0.25);
                break;

            case 'h':
                turn(0, 7, 6, 0.5);
                break;

            case 'i':
                turn(1, 7, 6, 0.25);
                break;

            case 'j':
                turn(0, 9, 8, 0.25);
                break;

            case 'k':
                turn(0, 9, 8, 0.5);
                break;

            case 'l':
                turn(1, 9, 8, 0.25);
                break;

            case 'm':
                turn(0, 11, 10, 0.25);
                break;

            case 'n':
                turn(0, 11, 10, 0.5);
                break;

            case 'o':
                turn(1, 11, 10, 0.25);
                break;

            case 'z':
                Serial.write("DN");
                delay(1000);
                break;

            }
            // Serial.write(inData[i]);
        }
    }
}

void turn(int sens, int pinPas, int pinSens, float rot) {

    digitalWrite(pinSens, sens);

    for(int k = 0; k < spr * rot; k++){
        digitalWrite(pinPas, HIGH);
        delayMicroseconds(50); // ?
        digitalWrite(pinPas, LOW);
        delayMicroseconds(50);
    }
}
