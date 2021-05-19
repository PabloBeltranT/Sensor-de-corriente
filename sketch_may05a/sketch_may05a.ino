void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT), pinMode(9, OUTPUT), pinMode(13, OUTPUT);
}


void imprimir(String mensaje, int cajas){
  Serial.print(mensaje), Serial.println(cajas);
}

float entrada, 
      voltaje, 
      resistencia = 0.9, 
      corriente;

void lectura(){
  
  float muestra=0;
  for(int i=0; i<=50; i++){
    entrada = analogRead(A1);
    voltaje = entrada * 6 / 1024;
    corriente = voltaje / resistencia;
    muestra = muestra + voltaje;
  }
  muestra = (muestra / 50) * 2;
  Serial.println(muestra, 4);
}


void loop() {

  char in = Serial.read();

  switch(in){
    case 'a':
      lectura();
    break;

    case 'b':
      digitalWrite(13, LOW);
    break;

    case 'c':
      digitalWrite(13, HIGH);
    break;
  }

}
