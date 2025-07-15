import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def getDistance():
  trig_pin = 23
  echo_pin = 24
  GPIO_setup(trig_pin,GPIO.OUT)
  GPIO_setup(echo_pin,GPIO.IN)

  GPIO.output(trig_pin,False)
  time,sleep(1)
  GPIO.output(trig_pin,True)
  time,sleep(0.00001)
  GPIO.output(trig_pin,False)

  while GPIO.input(echo_pin) == 0:
    start = time.time()

  while GPIO.input(echo_pin) == 1:
    end = time.time()

  duration = end - start
  distance = duration * 17150
  distance = round(distance,2)
  GPIO.cleanup()
  return distance

print "Distance: ", getDistance(), "cm"













