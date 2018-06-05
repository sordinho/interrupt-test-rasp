#Created by Davide Sordi in 05/06/2018 at 21.05
from time import sleep

import RPi.GPIO as GPIO

def interruptReceived():
	print("############ INTERRUPT ############")

def main():
	while True:
		print("Waiting for interrupt")
		sleep(2)


if __name__ == "__main__":
	interrupt_pin = 2
	GPIO.setup(interrupt_pin, GPIO.IN)  # Acqua
	GPIO.add_event_detect(interrupt_pin, GPIO.RISING, callback=interruptReceived)
	main()