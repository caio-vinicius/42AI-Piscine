import random

number = random.randrange(0, 99)
end = 1
attempts = 0

while end:
	while end:
		guessing = input("What's your guess between 1 and 99?\n>> ")
	
		if not guessing.isnumeric():
			print ("That's not a number")
		else:
			end = 0
	end = 1

	if int(guessing) > number:
		print ("Too high!")
	elif int(guessing) < number:
		print ("Too low!")
	elif int(guessing) == number:
		attempts += 1
		print ("Congrats! You've got it.\nYou won in", attempts,"attempts")
		end = 0

	attempts += 1
