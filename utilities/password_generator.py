import random


def target_password():
	upper = ""
	lower = ""
	numbers = ""
	extra_chars = ""
	password_str = ""
	for j in range(1, 140):
		if j in range(48, 58):
			numbers += chr(j)
		elif j in range(65, 91):
			upper += chr(j)
		elif j in range(97, 123):
			lower += chr(j)
		elif j in range(33, 48):
			extra_chars += chr(j)
		else:
			pass
	try:
		length = int(input("Enter password length (8-25): "))
		upper_case = input("Do you want Capital letters(Y/N)").upper()
		lower_case = input("Do you want Small letters(Y/N)").upper()
		digits = input("Do you want Numbers(Y/N)").upper()
		characters = input("Do you want Characters (Y/N)").upper()
		
		if upper_case == "Y":
			uppercase = True
		else:
			uppercase = False
		if lower_case == "Y":
			lowercase = True
		else:
			lowercase = False
		if digits == "Y":
			nums = True
		else:
			nums = False
		if characters == "Y":
			extras = True
		else:
			extras = False
		
		if 25 >= length > 8:
			pass
			if uppercase:
				password_str += upper
			if lowercase:
				password_str += lower
			if nums:
				password_str += numbers
			if extras:
				password_str += extra_chars
		else:
			pass
		
		password = "".join(random.sample(password_str, length))
		return f"Your Password is: '{password}'"
	except:
		print("Invalid Input \nMaybe check length")
print(target_password())

input()
