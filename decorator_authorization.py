def is_root(in_func):
	def wrapper(user):
		print("Deleting files...")
		if user.get("allow"):
			in_func(user)
		else:
			print("Oops, you are NOT root\n")
			return 0
		print("Deleted all files!\n")
	return wrapper

@is_root
def delete_files(user):
	print("Success")

users = [
	{"name": "admin", "allow": True},
	{"name": "user5", "allow": False},
	{"name": "hacker", "allow": False},
	{"name": "user33", "allow": True},
	{"name": "grandma", "allow": False}
	]

if __name__ == "__main__":
	for user in users:
		delete_files(user)
