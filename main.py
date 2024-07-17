import random
from art import logo, vs
from game_data import data


def no_duplicates(first, second):
	while first == second:
		second = data[random.randint(0, len(data) - 1)]


def compare_followers(person_one, person_two):
	higher_number = 0
	if person_one.get('follower_count') > person_two.get('follower_count'):
		higher_number = person_a.get('follower_count')
	elif person_one.get('follower_count') < person_two.get('follower_count'):
		higher_number = person_b.get('follower_count')
	return higher_number


def versus():
	print(
		f"Compare A: {person_a.get('name')}, a {person_a.get('description')}, from {person_a.get('country')}.")
	print(vs)
	print(
		f"Against B: {person_b.get('name')}, a {person_b.get('description')}, from {person_b.get('country')}.")


# Main Code
start = input("Do you want to play 'Higher or Lower'? ").lower()
if start == 'yes':
	game_start = True
else:
	game_start = False
	print('Maybe next time.\nGoodbye.')

score = 0
while game_start:
	person_b = data[random.randint(0, len(data) - 1)]
	correctness = False
	game_on = True
	while game_on:
		print(logo)
		if correctness:
			score += 1
			print(f"\nThat's Right! Current score: {score}")
		person_a = person_b
		person_b = data[random.randint(0, len(data) - 1)]
		versus()
		no_duplicates(person_a, person_b)
		more_followers = compare_followers(person_a, person_b)
		choice = input("Who has more followers? Type 'A' or 'B': ").lower()
		if (choice == 'a' and more_followers == person_a.get(
				'follower_count')) or (
				choice == 'b' and more_followers == person_b.get(
			'follower_count')):
			correctness = True
		else:
			print(f"\nSorry, that's wrong. Final score: {score}")
			correctness = False
			game_on = False

	restart_game = input("\nDo you want to play again? ").lower()
	reset = True
	while reset:
		if restart_game == "yes":
			game_start = True
			score = 0
			reset = False
		elif restart_game == "no":
			game_start = False
			reset = False
			print("Goodbye.")
		else:
			print("Invalid Input.\n")
			restart_game = input("\nDo you want to play again? ").lower()
