import random
import time
from functions import *
def story():
	choice = ""
	loop = 0

	printf("Welcome to the Train Mystery game!")
	time.sleep(1)

	while True:
		name = input("Choose your name: ")
		for i in name:
			loop += 1
		if loop < 4:
			print("Non valid name")
			continue
		loop = 0
		break	
	inputf(f"Hi {name}!, pleased to meet you!...v")
	time.sleep(0.5)

	inputf("My name is Luke Atmey and I need you to go to the insert your city name here...v")
	inputf("You'll take a train that will take you to that location...v")
	inputf("Good luck!..v")

	dateprint("14 SEPTEMBER 1990, 6:00 AM...v")
	inputf("The train is near...v")
	printf("Do you want to get in?\n[1] Yes\n[2] Yes")
	choicef()
	printf("You get into the train and take a sit")

	story = random.randrange(1,3)
	if story == 1:
		inputf("You sit next to someone not very friendly, bad luck...v")
		inputf(
		"You  can't see the person's face but you see that the person next to you has a knife on his pocket...v"
		)
		time.sleep(1)
		printf("What do you do?")
		time.sleep(0.5)
		printf(
		"[1] Ask him why does he have a knife\n[2] Scream that he has a knife\n[3] Try changing your seat\n[4] Don't do anything"
		)
		choicef()

		while True:
			if choice == 1:
				printf("You ask why does he have a knife")
				time.sleep(1)
				printf("No answer...")
				continue
			if choice == 2:
				printf("You scream at loud thaty he has a knife")
				time.sleep(0.5)
				printf("Everyone on the train starts wondering what is going on")
				time.sleep(0.5)
				printf("Suddendly, the lights on the train go off, no one can see anything")
				time.sleep(0.5)
				printf(
				"Someone is dead, everything is so fast that anyone remember the face of anyone, no one knows who's the killer..."
				)
			if choice == 4 and loop == 0:
				printf("You don't do anything...")
				time.sleep(3)
				printf("Nothing happens...")
				loop+=1
				continue
			if choice == 4 and loop == 1:
				printf("You still don't do anything...")
				time.sleep(3)
				printf("Why are you doing nothing?")
				loop+=1
				continue
			if choice == 4 and loop == 2:
				printf("You aren't doing anything still...")
				time.sleep(3)
				printf(".............")
				loop+=1
				continue
			if choice == 4 and loop == 3:
				printf("You again don't do anything...")
				time.sleep(3)
				printf("Suddendly, the lights are off and you can't see anything")
				printf("The lights go on again but...")
				story = random.randrange(1,3)
	else:
		printf("You sit next to someone very friendly, good luck!...v")
story()
