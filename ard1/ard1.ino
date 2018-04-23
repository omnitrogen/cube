/*
toujours brancher l'alim en stad by avant à la carte arduino (+3.3V)

*/

//int PAUSE = 0;         //0/32 ;
int pasParTour = 200*32 ;
int messageRecu = "";
int messageTraduitEnNbDuMoteur ;
// bool reception = 0;

int sensMoteur;
int pinPas;
int pinSens;
float rotation;
int mouvement;

bool FIN=LOW;

void setup(){
    Serial.begin(9600);
    Serial.println("   ---   Programme de resolution du Cube 3*3*3   ---   ");
    Serial.println("DEBUT : Initialisation ");
    for (int i=0 ; i!=10 ; i++){
        pinMode(i, OUTPUT);
        digitalWrite(i,LOW);
    }
    pinMode(10,OUTPUT);
    digitalWrite(10,HIGH);
    pinMode(11,OUTPUT);
    digitalWrite(11,LOW);
    pinMode(12,OUTPUT);
    digitalWrite(12,HIGH);
    delay(1000);
  
    Serial.println("        Initialisation terminee ");
    Serial.println(" ");
}

void loop(){
    if (Serial.available())  {
        messageRecu = byte(Serial.read());
        switch (messageRecu) {
            case 'a':
              messageTraduitEnNbDuMoteur = 1 ;
              sensMoteur = 0;
              pinPas= 1;
              pinSens=0;
              break;
            case 'b':
              messageTraduitEnNbDuMoteur = 1 ;
              sensMoteur = 2;
              pinPas= 1;
              pinSens=0;           
              break;
            case 'c':
              messageTraduitEnNbDuMoteur = 1 ;
              sensMoteur = 1;
              pinPas= 1;
              pinSens=0;              
              break;
            case 'd':
              messageTraduitEnNbDuMoteur = 2 ;
              sensMoteur = 0;
              pinPas= 3;
              pinSens=2;              
              break;
            case 'e':
              messageTraduitEnNbDuMoteur = 2 ;
              sensMoteur = 2;
              pinPas= 3;
              pinSens=2;              
              break;
            case 'f':
              messageTraduitEnNbDuMoteur = 2 ;
              sensMoteur = 1;
              pinPas= 3;
              pinSens=2;              
              break;
            case 'g':
              messageTraduitEnNbDuMoteur = 3 ;
              sensMoteur = 0;
              pinPas= 5;
              pinSens=4;              
              break;
            case 'h':
              messageTraduitEnNbDuMoteur = 3 ;
              sensMoteur = 2;
              pinPas= 5;
              pinSens=4;              
              break;
            case 'i':
              messageTraduitEnNbDuMoteur = 3 ;
              sensMoteur = 1;
              pinPas= 5;
              pinSens=4;              
              break;
            case 'j':
              messageTraduitEnNbDuMoteur = 4 ;
              sensMoteur = 0;
              pinPas= 7;
              pinSens=6;              
              break;
            case 'k':
              messageTraduitEnNbDuMoteur = 4 ;
              sensMoteur = 2;
              pinPas= 7;
              pinSens=6;              
              break;
            case 'l':
              messageTraduitEnNbDuMoteur = 4 ;
              sensMoteur = 1;
              pinPas= 7;
              pinSens=6;              
              break;
            case 'm':
              messageTraduitEnNbDuMoteur = 5 ;
              sensMoteur = 0;
              pinPas= 9;
              pinSens=8;              
              break;
            case 'n':
              messageTraduitEnNbDuMoteur = 5 ;
              sensMoteur = 2;
              pinPas= 9;
              pinSens=8;              
              break;
            case 'o':
              messageTraduitEnNbDuMoteur = 5 ;
              sensMoteur = 1;
              pinPas= 9;
              pinSens=8;              
              break;
            case 'z':
              FIN = HIGH;
              Serial.println(" ");
              Serial.println(" FIN --> Cube resolu ");
              Serial.println(" ---   Fin Programme de resolution du Cube 3*3*3   --- ");
              break;
            }
    }     //Fin du    if (Serial.available())  {

    if(FIN == LOW){
        if(messageRecu != ""){
            //pinPas=(messageTraduitEnNbDuMoteur*2)-1 ;
            //pinSens=(messageTraduitEnNbDuMoteur*2)-2 ;
            rotation = 0.25 ;               // simple mouvement QUART DE TOUR
            if (sensMoteur == 2) {      //si double mouvement DEMI TOUR
                rotation = 0.5;
                sensMoteur=1;
            }

            Serial.print("  pinPas : ");
            Serial.print(pinPas);
            Serial.print(" - pinSens : ");
            Serial.print(pinSens);
            Serial.print(" - rotation : ");
            Serial.print(rotation);
            Serial.print(" - sensMoteur : ");
            Serial.println(sensMoteur);
            
            digitalWrite(pinSens,sensMoteur); // selection du sens sur le pin Sens du moteur

            mouvement = pasParTour*rotation ;
            Serial.print("  -  mouvement");
            Serial.println(mouvement);
            for(int k=0; k!=mouvement; k++){
                    digitalWrite(pinPas,HIGH);   
                    //delay(PAUSE);
                    digitalWrite(pinPas,LOW);     
                    //delay(PAUSE);
                }
                
          //Serial.println("OK");   
          messageRecu = "" ;
          delay(1);
        }    //Fin de      if(messageRecu!=""){
    }
    while (FIN){
        delay(10000);
    }
}
