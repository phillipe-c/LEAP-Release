
# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

#########################################################
#  LISA LEDs Handler (LLH)
#  
#  Created by Phillipe Caetano.
#  Copyright © 2021 Phillipe Caetano. All rights reserved.
##########################################################

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT) # set GPIO 26 as output for led  
GPIO.setup(6, GPIO.OUT)
led = GPIO.PWM(26,100)   # create object led for PWM on port 26 at 100 Hertz  
ledred = GPIO.PWM(6, 100)
led.start(0)
ledred.start(0)
pause_time=0.2

class GradLed():
    """The gradual led activator for the Pi. Uses the GPIO pins 26 and 6"""

    def __init__(self):
        super().__init__()          

    def grad_turn_on(pause_time=0.002):
        """Turns the main leds connected to GPIO Pin 26 gradually on. You can confugure the time by changing 'pause_time'."""
        for i in range(0,101):
            led.ChangeDutyCycle(i)  
            sleep(pause_time)

    def grad_turn_off(pause_time=0.002, with_led_on=False):
        """Turns the main leds connected to GPIO Pin 26 gradually off. You can confugure the time by changing 'pause_time'."""
        if (with_led_on == True) or (GPIO.input(26) == 0):
            for i in range(0,101):   
                led.ChangeDutyCycle(i)
                sleep(pause_time)
        for i in range(100,-1,-1):
            led.ChangeDutyCycle(i)
            sleep(pause_time)

    def grad_turn_on_and_off(pause_time=0.002):
        for i in range(0,101):    
            led.ChangeDutyCycle(i)
            sleep(0.0035)
        sleep(0.002)
        for i in range(100,-1,-1): # from 100 to zero in steps of -1 
            led.ChangeDutyCycle(i)
            sleep(0.001)
        sleep(0.001)
        for i in range(0,101): 
            led.ChangeDutyCycle(i)
            sleep(0.0035)
        sleep(0.002)    
        for i in range(100,-1,-1): 
            led.ChangeDutyCycle(i)
            sleep(0.001)
    
    def error_msg_led(pause_time=0.002, with_led_on=False):
        """Turns the main leds connected to GPIO Pin 6 gradually on and off (they blink 2 times). You can confugure the time by changing 'pause_time'."""
        if (with_led_on == True) or (GPIO.input(26) == 1):
            for i in range(100,-1,-1):   
                led.ChangeDutyCycle(i)
                sleep(pause_time)
        for i in range(0,101):   
            ledred.ChangeDutyCycle(i)
            sleep(0.002)
        for i in range(100,-1,-1):   
            ledred.ChangeDutyCycle(i)
            sleep(0.002)
        for i in range(0,101):   
            ledred.ChangeDutyCycle(i)
            sleep(0.002)
        for i in range(100,-1,-1):   
            ledred.ChangeDutyCycle(i)
            sleep(0.002)    
            
    def respond_led(with_led_on=False, pause_time=0.002):
        """Activates the response animation on the LEDs"""
        if (with_led_on == True) or (GPIO.input(26) == 1):
            for i in range(100,-1,-1):   
                led.ChangeDutyCycle(i)
                sleep(pause_time)
        for i in range(0,101):   
            led.ChangeDutyCycle(i)
            sleep(0.0035)
        for i in range(100,-1,-1):   
            led.ChangeDutyCycle(i)
            sleep(0.003)
        for i in range(0,101):   
            led.ChangeDutyCycle(i)
            sleep(0.0035)

    def red_led(led_mode, pause_time=0.002):
        """Turns the main leds connected to GPIO Pin 6 gradually on or off (True for on, and False for off). You can confugure the time by changing 'pause_time'."""
        if (GPIO.input(6) == 1) and (led_mode == True):
            for i in range(100,-1,-1):   
                ledred.ChangeDutyCycle(i)
                sleep(pause_time)
        if (led_mode == True):
            for i in range(0, 101):   
                ledred.ChangeDutyCycle(i)
                sleep(pause_time)
        if (led_mode == False):
            for i in range(100, -1, -1):   
                ledred.ChangeDutyCycle(i)
                sleep(pause_time)