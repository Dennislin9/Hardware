#include <IRremote.h>

const int IR = 8;
const int ledPins[] = {7, 6, 5, 4};

int knipperTimes[] = {500, 500, 0, 0};
int lastTime = 0;
int currentLed = 0;
int knippert = 2;
int gekoppeld = 0;

long int knop0 = 16732845;
long int knop1 = 16724175;
long int knop2 = 16718055;
long int knop3 = 16743045;
long int knop4 = 16716015;

int num_0 = 0xFF6897;
#define  NUM1 0xFF30CF

unsigned long lastTimes[] = {0, 0, 0, 0};

int ledStatus[] = {LOW, LOW, LOW, LOW};
int led = LOW;
IRrecv irrecv(IR);
decode_results results;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn();
  for(int i : ledPins) {
    pinMode(i, OUTPUT);
  }
 
}

void loop(){
  if(millis() - lastTime >= 100) {                                    
    lastTime = millis();                                              
    if(irrecv.decode(&results)) {                                    
      irrecv.resume();                                                
     
      if(currentLed == 0) {                                           
                                        
          if((results.value) == (knop1)) {                       
            currentLed = 1;                                           
          } else if  ((results.value) == (knop2)) {                       
            currentLed = 2; 
          }
          else if  ((results.value) == (knop3)) {                       
            currentLed = 3; 
          }
          else if  ((results.value) == (knop4)) {                       
            currentLed = 4; 
          }
      } else {
        
                                   
          if((results.value) == (knop0)) {                       
            X(0);                                                    
          } else if((results.value) == (knop1)) {                       
            X(1);                                                    
          }else if((results.value) == (knop2)) {                       
            X(2);                                                    
          }
          else if((results.value) == (knop3)) {                       
            X(3);                                                    
          }
          else if((results.value) == (knop4)) {                       
            X(4);                                                    
          }
          
       
      }
    }
  }
  for(int i : ledPins) {
    i = i-4;
    if(millis() - lastTimes[i] >= knipperTimes[i] && knipperTimes[i] != 0) {
      lastTimes[i] = millis();
      ledStatus[i] = (ledStatus[i] == LOW) ? HIGH : LOW;
      digitalWrite(ledPins[i], ledStatus[i]);                         
    } else if(knipperTimes[i] == 0) {
      digitalWrite(ledPins[i], LOW);                                  
    }
  }
}

void X(int mode) {
  if(mode == 0) {
    knippert = 0;
    for(int i : knipperTimes) {
      if(i != 0) {
        knippert++;                                                  
      }
    }
  }
  if(mode != 0 || knippert > 2) {
    knipperTimes[currentLed-1] = mode * 100;                          
    currentLed = 0;                                                   
                                                                      
  }
}
