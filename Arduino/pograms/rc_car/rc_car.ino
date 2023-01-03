// C++ code
//
void setup()
{
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(3, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()){
    String car_input=Serial.readStringUntil('\n');
    if(car_input=="start"){
      digitalWrite(11,HIGH);
      digitalWrite(3,HIGH);
      Serial.println(car_input);

    }
    else if(car_input=="fw"){
      digitalWrite(10,HIGH);
      digitalWrite(3,HIGH);
      digitalWrite(9,LOW);
      digitalWrite(6,LOW);
      Serial.println(car_input);
    }
    
    else if(car_input=="lt"){
      //Left Motar
      digitalWrite(11,LOW);
      delay(2000);
      digitalWrite(11,HIGH);
      Serial.println(car_input);

    }
    else if(car_input=="rt"){
      //Right Motar
      digitalWrite(3,LOW);
      delay(2000);
      digitalWrite(3,HIGH);
      Serial.println(car_input);
    }
    else if(car_input=="br"){
      digitalWrite(10,LOW);
      digitalWrite(5,LOW);
      digitalWrite(9,LOW);
      digitalWrite(6,LOW);
      Serial.println(car_input);
    }
    else if(car_input=="bw"){
      digitalWrite(9,HIGH);
      digitalWrite(6,HIGH);
      digitalWrite(10,LOW);
      digitalWrite(5,LOW);
      Serial.println(car_input);

    }
    else if(car_input=="stop"){
      digitalWrite(11,LOW);
      digitalWrite(3,LOW);
      Serial.println(car_input);
    }
    else{
      Serial.println("Wrong Input");
      Serial.println(car_input);
    }
  }
}
