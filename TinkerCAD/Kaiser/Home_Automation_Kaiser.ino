float temp;
const int buzzer = 9;
void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(A0, INPUT);
  Serial.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
  delay(1000);
}


void loop()
{
  digitalWrite(3, LOW);
  int read=digitalRead(2);
  if(read == HIGH)
  {
    digitalWrite(3,HIGH);
    delay(1000); 
  }
  temp = analogRead(A0);
  temp =((temp*5)/1024);
  temp = (temp-0.5)*100;
  Serial.print("Temperature = ");
  Serial.println(temp);
  if (temp <= 35) 
  {
    digitalWrite(3, HIGH);
    noTone(buzzer);
    delay(2000);
  }
  else
  {
    digitalWrite(3, LOW);
    tone(buzzer, 2000);
    delay(2000);
  }
}
