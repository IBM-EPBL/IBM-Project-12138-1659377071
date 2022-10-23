import random

def detect_alarm():
    print("Alarm ringing")


x = (random.random())*50  # in celcius
y = (random.random())*100

if (x > 40):
    detect_alarm()