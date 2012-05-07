/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */  
 
char input;

void setup() {                
  // initialize the digital pin as an output.
  // Pin 13 has an LED connected on most Arduino boards:
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  Serial.begin(38400);
  Serial.flush();  
}

void loop() {
  
  input = Serial.read();
  if (input == '-1') {}

  else
  {
    
    if (input == '2') 
    { 
      digitalWrite(2, HIGH);
      delay(50);
      digitalWrite(2, LOW);
    }
    
    if (input == '3') 
    { 
      digitalWrite(3, HIGH);
      delay(50);
      digitalWrite(3, LOW);
    }
    
  }
}
