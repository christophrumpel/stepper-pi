#!/usr/bin/python

from Stepper import Motor
from time import sleep
import RPi.GPIO as GPIO
import sys


if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)

	m = Motor([18,23,24,25], 15)

	# clock 180
	m.move_to(0)
	sleep(5)
	m.move_to(180)
	sleep(5)
	m.move_to(90)
	sleep(5)
	m.move_to(-90)
	GPIO.cleanup()

