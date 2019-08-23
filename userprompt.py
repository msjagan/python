count = 1
tries = 3

users = [{
	'username': 'jagan',
	'password': 'jagan'
}, {
	'username': 'siddiq',
	'password': 'siddiq'
}]




username = input("Enter username: ")

while count < tries:
	for x in range(0, len(users)):
		if username == users[x]['username']:
			print("Login Success")
			break
		else:
			if count == tries - 1:
				print("This is last try")
			username = input("Enter username again: ")
	count = count + 1
if count == tries:
	print("Out of tries")