import sys
import random

balance = 5000

choose0 = input('Start a game? [y]es or [n]o : ')

print(f'Your start balance = {balance}')

def game(balance):

	if choose0 == 'n':
		sys.exit()
	else:
		choose1 = int(input('How much do you bet?: '))
		if balance >= choose1 and balance != 0:

			answ1 = random.choice([0,1,2,3,4,5,6,7,8,9])
			answ2 = random.choice([0,1,2,3,4,5,6,7,8,9])

			choose2 = input('Choose beetwen even and odd numbers (Cho and Han):\n[c]ho or [h]an: ')

			if (answ1 + answ2) % 2 == 0:
				if choose2 == 'c':
					balance += choose1
					print(f'WON, your current balance = {balance}')
					game(balance)
				else:
					balance -= choose1
					print(f'LOSER, your current balance = {balance}')
					game(balance)
			else:
				if choose2 == 'h':
					balance += choose1
					print(f'WON, your current balance = {balance}')
					game(balance)
				else:
					balance -= choose1
					print(f'LOSER, your current balance = {balance}')
					game(balance)
		else:
			print('Sorry, not enough money..')
			sys.exit()

if __name__ == '__main__':
	game(balance)

