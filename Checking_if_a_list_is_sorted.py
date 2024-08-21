# Python3 code to demonstrate 
# to check if list is sorted
# using sort()
 
# initializing list
test_list = [10]
 
# printing original list 
print ("Original list : " + str(test_list))
 
# using sort() to 
# check sorted list 
flag = 0
test_list1 = test_list[:]
test_list1.sort()
if (test_list1 == test_list):
    flag = 1
     
# printing result
if (flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")