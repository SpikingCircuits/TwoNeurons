/*
  Arduino code for the simple neural networks.
  Basically receive events via the serial port and make the corresponding LED blink
 */  
 
char input;

void setup() {                
  // Init output pins
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);

  // Init serial port
  Serial.begin(38400);
  Serial.flush();  
}

void loop() {
  
  // Read serial port
  input = Serial.read();
  if (input == '-1') {}

  else
  {
    
    // Send to pin 2
    if (input == '2') 
    { 
      digitalWrite(2, HIGH);
      delay(50);
      digitalWrite(2, LOW);
    }
    
    // Send to pin 3
    if (input == '3') 
    { 
      digitalWrite(3, HIGH);
      delay(50);
      digitalWrite(3, LOW);
    }
    
  }
}
