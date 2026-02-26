import random
import string
from itertools import permutations
from itertools import combinations


# chars = string.ascii_letters + string.digits + string.punctuation
# wrote my own character instead of using the string module
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z','1','2','3','4','5','6','7','8','9','0', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';','<', '=', '>', '?', '@','{', '|', '}', '~']

password = input("Enter a Pin: \n")
# password = "ABCDEFGHI!@"	# This is found faster when using the chars in the list

num = 1
while num < 2:
	perm = permutations(chars,len(password))
	password_2 = tuple(password)
	if 8 <= len(password) <= 12:
		print("Searching...")
		for i in perm:
			if i == password_2:
				str_i = ""
				for j in i:
					str_i += j
				print("The password is: ",str_i)
				num = 5
				break
	else:	
		print("Length of password Unmatched")
		break

input()

