import RPi.GPIO as GPIO
import time
from rrb2 import *

rr = RRB2() #实例电机控制器

def init_vehicle():
  rr.set_led1(1)

def turn_left(angle):
  rr.set_motors(1,1,1,0)
  time.sleep(angle/20)
  rr.set_motors(0,0,0,0)

def turn_right(angle):
  rr.set_motors(1,0,1,1)
  time.sleep(angle/20)
  rr.set_motors(0,0,0,0)

def forward(angle):
  rr.set_motors(1,1,1,1)
  time.sleep(angle/20)
  rr.set_motors(0,0,0,0)

def backward(angle):
  rr.set_motors(1,0,1,0)
  time.sleep(angle/20)
  rr.set_motors(0,0,0,0)

def stop():
  rr.set_motors(0,0,0,0)

def cleanup():
  GPIO.cleanup()

