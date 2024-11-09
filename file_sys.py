file = input('Enter a file name: ')
option = input('Open [b]inary or [t]ext: ')

if option == 'b':
	with open(file, 'rb') as f:
		show = f.read()
		print(show)
		print(f'\n{show.count(b'\n')} lines')
else:
	with open(file, 'r') as f:
		show = f.read()
		print(show)
		print(f'\n{show.count('\n')} lines')
