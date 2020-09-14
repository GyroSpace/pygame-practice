import random
import time
from functions import *

printf("Welcome to the Train Mystery game!")
time.sleep(1)

while True:
	name = inputf("Choose your name: ")
	if len(name) < 4:
		print("Please enter at least 4 characters")
		continue
	break
printf(f"Hi {name}!, pleased to meet you!")
time.sleep(0.5)

inputf("My name is Luke Atmey and I need you to go to the insert your city name here...v")
inputf("You'll take a train that will take you to that location...v")
inputf("Good luck!..v")

dateprint("14 SEPTEMBER 1990, 6:00 AM...v")
inputf("The train is near")
inputf("Do you want to get in?\n[1] Yes\n[2] Yes")
while True:
	try:
		choice = int(input("Select a option: "))
	except ValueError:
		print("You entered a non-valid character, try again")
		continue
	if choice > 2 or choice < 1:
		print("You entered a non-valid number, try again")
		continue
	break


