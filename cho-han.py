import sys
import random

balance = 5000

choose0 = input('\nStart a game? [y]es or [n]o : ')

print(f'\nYour start balance = {balance}')

def game(balance):

	if choose0 == 'n':
		sys.exit()
	else:
		choose1 = int(input('\nHow much do you bet?: '))
		if balance >= choose1 and balance != 0:

			answ1 = random.choice([0,1,2,3,4,5,6,7,8,9])
			answ2 = random.choice([0,1,2,3,4,5,6,7,8,9])

			choose2 = input('\nChoose beetwen even and odd numbers (Cho and Han):\n[c]ho or [h]an: ')

			if (answ1 + answ2) % 2 == 0:
				if choose2 == 'c':
					balance += choose1
					balance -= 40 
					print(f'\nWON, your current balance = {balance}\nHouse collects 40')
					game(balance)
				else:
					balance -= choose1
					balance -= 40 
					print(f'\nLOSER, your current balance = {balance}\nHouse collects 40')
					game(balance)
			else:
				if choose2 == 'h':
					balance += choose1
					balance -= 40 
					print(f'\nWON, your current balance = {balance}\nHouse collects 40')
					game(balance)
				else:
					balance -= choose1
					balance -= 40 
					print(f'\nLOSER, your current balance = {balance}\nHouse collects 40')
					game(balance)
		else:
			print('Sorry, not enough money..')
			sys.exit()

if __name__ == '__main__':
	game(balance)

