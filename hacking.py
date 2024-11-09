import sys

pass_list = ('RESOLVE', 'CHICKEN', 'ADDRESS', 'DISPLAY', 'PENALTY', 'REFUGEE', 'IMPROVE')
attempts = 5

def hack(pass_list, attempts):

	if attempts == 0:
		print('Sorry, ciao')
		sys.exit()

	variety = input('Enter a password:\n')

	if variety not in pass_list:
	    print('NOT close')
	    attempts -= 1
	    hack(pass_list, attempts)

	elif variety in pass_list and variety != pass_list[-1]:
	    right_pass = 'IMPROVE'
	    count = sum(1 for i in range(min(len(variety), len(right_pass))) if variety[i] == right_pass[i])
	    print(f"Matches: {count}/7")
	    attempts -= 1
	    hack(pass_list, attempts)

	else:
	    print('Password is IMPROVE')

if __name__ == '__main__':
	hack(pass_list, attempts)
