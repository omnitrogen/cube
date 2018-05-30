String inData;
const int spr = 200 * 32;

void setup() {
    Serial.begin(9600);

    for (int i=2; i<12; i++){
        pinMode(i, OUTPUT);
        digitalWrite(i,LOW);
    }

    for (int i=14; i<19; i++){
        pinMode(i, OUTPUT);
        digitalWrite(i,HIGH);
    }

    delay(1000);
}

void loop() {

    if (Serial.available()) {

        inData = Serial.readString();

        for (int i = 0; i < inData.length(); i++) {
            switch (inData[i]) {

            case 'a':
                turn(0, 3, 2, 0.25, 14);
                break;

            case 'b':
                turn(0, 3, 2, 0.5, 14);
                break;

            case 'c':
                turn(1, 3, 2, 0.25, 14);
                break;

            case 'd':
                turn(0, 5, 4, 0.25, 15);
                break;

            case 'e':
                turn(0, 5, 4, 0.5, 15);
                break;

            case 'f':
                turn(1, 5, 4, 0.25, 15);
                break;

            case 'g':
                turn(0, 7, 6, 0.25, 16);
                break;

            case 'h':
                turn(0, 7, 6, 0.5, 16);
                break;

            case 'i':
                turn(1, 7, 6, 0.25, 16);
                break;

            case 'j':
                turn(0, 9, 8, 0.25, 17);
                break;

            case 'k':
                turn(0, 9, 8, 0.5, 17);
                break;

            case 'l':
                turn(1, 9, 8, 0.25, 17);
                break;

            case 'm':
                turn(0, 11, 10, 0.25, 18);
                break;

            case 'n':
                turn(0, 11, 10, 0.5, 18);
                break;

            case 'o':
                turn(1, 11, 10, 0.25, 18);
                break;

            }
        }
    }
}

void turn(int sens, int pinPas, int pinSens, float rot, int enable) {

    digitalWrite(enable, LOW);
    delay(100);
    digitalWrite(pinSens, sens);
    delay(100);
    for(int k = 0; k <= spr * rot; k++){
        digitalWrite(pinPas, HIGH);
        // delayMicroseconds(10);
        digitalWrite(pinPas, LOW);
        delayMicroseconds(10);
    }
    delay(200);
    digitalWrite(enable, HIGH);
    delay(200);
}
