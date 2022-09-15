float t;
const int buz = 9;
void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(A0, INPUT);
  Serial.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(buz, OUTPUT);
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
  t = analogRead(A0);
  t =((temp5)1024);
  t = (t-0.5)100;
  Serial.print(Temperature = );
  Serial.println(t);
  if (t = 35) 
  {
    digitalWrite(3, HIGH);
    noTone(buz);
    delay(2000);
  }
  else
  {
    digitalWrite(3, LOW);
    tone(buz, 2000);
    delay(2000);
  }
}
