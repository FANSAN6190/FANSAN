// C++ code
//
void setup()
{
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()){
    String car_input=Serial.readStringUntil('\n');
    if(car_input=="start"){
      digitalWrite(5,HIGH);
      digitalWrite(3,HIGH);
      Serial.println("START");
    }
    else if(car_input=="fw"){
      digitalWrite(10,LOW);
      digitalWrite(6,LOW);
      digitalWrite(11,HIGH);
      digitalWrite(9,HIGH);
      //digitalWrite(11,LOW);
      //digitalWrite(9,LOW);
      Serial.println("forward");
    }
    
    else if(car_input=="lt"){
      //Left
      digitalWrite(5,LOW);
      delay(2000);
      digitalWrite(5,HIGH);
      Serial.println("left");
    }
    else if(car_input=="rt"){
      //Right Motar
      digitalWrite(3,LOW);
      delay(2000);
      digitalWrite(3,HIGH);
      Serial.println("right");
    }
    else if(car_input=="br"){
      digitalWrite(11,LOW);
      digitalWrite(9,LOW);
      digitalWrite(10,LOW);
      digitalWrite(6,LOW);
      Serial.println("break");
    }
    else if(car_input=="bw"){
      digitalWrite(11,LOW);
      digitalWrite(9,LOW);
      digitalWrite(10,HIGH);
      digitalWrite(6,HIGH);
      Serial.println("backward");
      
    }
    else if(car_input=="stop"){
      digitalWrite(5,LOW);
      digitalWrite(3,LOW);
      Serial.println("STOP");
    }
    else{
      Serial.println("Wrong Input");
    }
  }
}
