import random
num=random.randint(1,100)
while(True):
	print("guess the no. between 1to 100")
	guess=input()
	i=int(guess)
	if(i==num):
		print("YOU WIN")
		break
	elif(i<=num):
		print("TRY HIGHER")
	elif(i>=num):
		print("TRY LOWER")
