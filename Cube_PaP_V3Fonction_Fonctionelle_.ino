/*
toujours brancher l'alim en stad by avant à la carte arduino (+3.3V)

*/

int PAUSE = 50;         //0/32 ;
int pasParTour = 200*32 ;
int messageRecu = "";
int messageTraduitEnNbDuMoteur ;
// bool reception = 0;

int sensMoteur ;
int pinPas;
int pinSens;
float rotation;
int mouvement;

bool FIN=LOW;

void setup(){
    Serial.begin(9600);
    Serial.println("   ---   Programme de resolution du Cube 3*3*3   ---   ");
    Serial.println("DEBUT : Initialisation ");
    for (int i=2 ; i!=12 ; i++){
        pinMode(i, OUTPUT);
        digitalWrite(i,LOW);
    }
    /*pinMode(10,OUTPUT);
    digitalWrite(10,HIGH);
    pinMode(11,OUTPUT);
    digitalWrite(11,LOW);
    pinMode(12,OUTPUT);
    digitalWrite(12,HIGH);*/
    delay(1000);
  
    Serial.println("        Initialisation terminee ");
    Serial.println(" ");
}

void loop(){
    if (Serial.available())  {
        messageRecu = byte(Serial.read());
        switch (messageRecu) {
            case 'a':
              messageTraduitEnNbDuMoteur = 6 ;
              sensMoteur = 0;
              pinPas= 11;
              pinSens=10;
              rotation = 0.25 ;
              break;
            case 'b':
              messageTraduitEnNbDuMoteur = 6 ;
              sensMoteur = 2;
              pinPas= 11;
              pinSens=10;   
              rotation = 0.5 ;
              break;
            case 'c':
              messageTraduitEnNbDuMoteur = 6 ;
              sensMoteur = 1;
              pinPas= 11;
              pinSens=10;  
              rotation = 0.25 ;
              break;
            case 'd':
              messageTraduitEnNbDuMoteur = 2 ;
              sensMoteur = 0;
              pinPas= 3;
              pinSens=2;  
              rotation = 0.25 ; 
              break;
            case 'e':
              messageTraduitEnNbDuMoteur = 2 ;
              sensMoteur = 2;
              pinPas= 3;
              pinSens=2; 
              rotation = 0.5 ;    
              break;
            case 'f':
              messageTraduitEnNbDuMoteur = 2 ;
              sensMoteur = 1;
              pinPas= 3;
              pinSens=2; 
              rotation = 0.25 ;      
              break;
            case 'g':
              messageTraduitEnNbDuMoteur = 3 ;
              sensMoteur = 0;
              pinPas= 5;
              pinSens=4;  
              rotation = 0.25 ; 
              break;
            case 'h':
              messageTraduitEnNbDuMoteur = 3 ;
              sensMoteur = 2;
              pinPas= 5;
              pinSens=4; 
              rotation = 0.5 ;
              break;
            case 'i':
              messageTraduitEnNbDuMoteur = 3 ;
              sensMoteur = 1;
              pinPas= 5;
              pinSens=4;
              rotation = 0.25 ;  
              break;
            case 'j':
              messageTraduitEnNbDuMoteur = 4 ;
              sensMoteur = 0;
              pinPas= 7;
              pinSens=6;   
              rotation = 0.25 ;
              break;
            case 'k':
              messageTraduitEnNbDuMoteur = 4 ;
              sensMoteur = 2;
              pinPas= 7;
              pinSens=6;  
              rotation = 0.5 ;
              break;
            case 'l':
              messageTraduitEnNbDuMoteur = 4 ;
              sensMoteur = 1;
              pinPas= 7;
              pinSens=6; 
              rotation = 0.25 ;  
              break;
            case 'm':
              messageTraduitEnNbDuMoteur = 5 ;
              sensMoteur = 0;
              pinPas= 9;
              pinSens=8; 
              rotation = 0.25 ;  
              break;
            case 'n':
              messageTraduitEnNbDuMoteur = 5 ;
              sensMoteur = 2;
              pinPas= 9;
              pinSens=8; 
              rotation = 0.5 ;  
              break;
            case 'o':
              messageTraduitEnNbDuMoteur = 5 ;
              sensMoteur = 1;
              pinPas= 9;
              pinSens=8;  
              rotation = 0.25 ; 
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
        if(messageRecu!=""){
            /*//pinPas=(messageTraduitEnNbDuMoteur*2)-1 ;
            //pinSens=(messageTraduitEnNbDuMoteur*2)-2 ;
            rotation = 0.25 ;               // simple mouvement QUART DE TOUR
            if (sensMoteur == 2) {      //si double mouvement DEMI TOUR
                rotation = 0.5;
                sensMoteur=1;
            }*/

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
            for(int k; k!=mouvement; k++){
                    digitalWrite(pinPas,HIGH);   
                    digitalWrite(pinPas,LOW);     
                    delayMicroseconds(PAUSE);
                }
          messageRecu = "" ;
          delay(1);
        }    //Fin de      if(messageRecu!=""){
    }
    
    while (FIN){
        delay(10000);
    }
}
