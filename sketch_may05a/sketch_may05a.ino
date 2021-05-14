void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);

}

void loop() {
  if (Serial.available() > 0){
    char estado = Serial.read();

    switch(estado){
      case 'a':
      digitalWrite(13, HIGH);
      break;
      case 'b':
      digitalWrite(13, LOW);
      break;
      case 'c':
      while(true){
        int voltaje = analogRead(A0);
        Serial.println(voltaje); 
      }
      break;
    }
  }

}
