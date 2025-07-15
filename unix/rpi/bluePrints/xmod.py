#xmod
import RPi.GPIO as GPIO
import time
from rrb2 import *

pwmPin = 18#pwm interface
dc = 10             #10%  占空比 of pwm 信号

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin,GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 320)  # 信号=320Hz
rr = RRB2() #实例电机控制器

pwm.start(dc)
rr.set_led1(1)

rr.set_motors(1,1,1,1)

print 'Loop, press CTRL C to exit.'

while 1:
    time.sleep(0.075)

pwm.stop()
GPIO.cleanup()

