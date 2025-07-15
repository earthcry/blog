#!/
#
import RPi.GPIO as GPIO
import time
from rrb2 import *
import tty
import sys
import termios
def getch():
  '''real-time get keyboard info'''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
    return ch
pwmPin = 18#pwm interface
dc = 10             #10%  占空比 of pwm 信号
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin,GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 320)  # 信号=320Hz
rr = RRB2() #实例电机控制器
pwm.start(dc)
rr.set_led1(1)
var = 'n'
speed1 = 0
speed2 = 0
direction1 = 1
direction2 = 1

while var != 'q':
    var = getch()
    if var == 'l':
        speed1 = 0.5
        direction2 = 1
    if var == 'r':
        speed2 = 0.5
        direction2 = 1
    if var == 's':
        speed2 = 0.1
        direction = 1
    if var == 'f':
        speed1 = 1
        direction1 = 1
    if var == 'b':
        speed1 = 1
        direction1 = 0
    rr.set_motors(speed1,direction1,speed2,direction2)
    time.sleep(0.1)

pwm.stop()
GPIO.cleanup()

