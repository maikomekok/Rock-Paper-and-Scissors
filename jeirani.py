import random

def game():

	computer_score=0
	user_score=0
	steps=0

	while True:
		possible_choices = ["rock","paper","scissors"]
		computer_choices = random.choice(possible_choices)
		user_choice = input("please input: rock, paper, or scissors   ")

		steps+=1


		if user_choice == "scissors" and computer_choices == "rock" or user_choice=="paper" and computer_choices=="scissors" or user_choice=="paper" and computer_choices=="rock":
				print(f"\nYou chose {user_choice}, computer chose {computer_choices}.\n")
				print("computer wins!")
				computer_score+=1
				

		elif user_choice=="scissors" and computer_choices=="paper" or user_choice == "rock" and computer_choices=="scissors" or user_choice == "rock" and computer_choices == "paper":
				print(f"\nYou chose {user_choice}, computer chose {computer_choices}.\n")
				print("You win!")
				user_score+=1
				

		elif user_choice == computer_choices:
				print(f"\nYou chose {user_choice}, computer chose {computer_choices}.\n")
				print("its a draw!")
				computer_score+=0.5
				user_score+=0.5
		else: 
			    print("Wrong input! please check your spelling!")
				

		if steps == 5:
			print(f"Your score:{user_score} VS Computer {computer_score}" )
			break
			
		
game()


