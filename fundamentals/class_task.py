
# Task 1: Filter numbers greater than 10 and cube them
numbers_32 = [12,21,32,132,4,3,11]
print([x**3 for x in list(filter(lambda i:i > 10 ,numbers_32 ))])


# Task 2: Filter Strings Containing a Specific Substring 'o'
#String = input("Enter your String:").split(' ')
String_lst = ["Hello","Name"]
print(list(filter(lambda i:'o' in i, String_lst)))


# Task 3: Filter and Double Odd Numbers
odd_doubled = [num* 2 for num in  list(filter(lambda x : x % 2 != 0,[i for i in range(1,20)]))]
print(odd_doubled)

# Task 4: Filter Negative Numbers and Calculate Absolute Values
lst_3 = [abs(i) for i in list(filter(lambda x: x<0 , [i for i in range(-10,10)]))]
print("The sum of",lst_3," is = ",sum(lst_3))

# Task 5: Filter and Convert Strings to Uppercase
lst_str = ["hello","The","a","name"]
upper_strings = list(filter(lambda x:len(x)>3,[i.upper() for i in lst_str]))
print(upper_strings)


# Bonus Task: Take a string input and find out how many occurences of each vowel  you have
input_str = input("Enter the String: ").lower()
vowls = ["a","e","i","o","u"]
lst_DJ = []
for i in input_str:
	for j in vowls:
		if i in j:
			lst_DJ.append(i)
print("a occurs ",lst_DJ.count('a')," times")
print("e occurs ",lst_DJ.count('e')," times")
print("i occurs ",lst_DJ.count('i')," times")
print("o occurs ",lst_DJ.count('o')," times")
print("u occurs ",lst_DJ.count('u')," times")

