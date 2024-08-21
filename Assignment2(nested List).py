# Flatten the nested list using list comprehension
# Given the below nested list create a new flattened list

nested_list = [[1,2,3], [4,5,6], [7,8,9]]
f_list = [i for sublist in nested_list for i in sublist]
print(f_list)

# for i in nested_list: 
#     print(i)
#     for num in i:
#         f_list.append(num)
# print(f_list)



user_1 = {'username':'kanyankah', 'id':1}
user_2 = {'username':'msmith','id':2 ,  'email': 'my@gmail.com'}
user_3 = {'username':'johniah','id':3 }
my_users = [user_1 , user_2 , user_3]

select_user = {}
user_lookup = 1
for user in my_users:
    if 'id' in user:
        if user['id'] == 2:
            select_user = user

print(select_user)


for x in range(0,10):
    for user in my_users:
        if user['id'] == x:
            print(user)

userr = [user for x in range(0,10) for user in my_users if user['id'] == x ]
print(userr)
