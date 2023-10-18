from random import *

x = randint(1,100)
b = True

print("""
Welcome to The Guessing Game. There will be a randomly generated number between 1 and 100, and your job is to guess the number. 
We will provide some tips to help you along the way. You have unlimited guesses. 
HAVE FUN!!
""")
while (b):
	ans = int(input("Please enter a guess: "))
	if ans < x:
		print("Too small")
	elif ans > x:
		print("Too big")
	elif ans == x:
		print("You got it")
		b = False
