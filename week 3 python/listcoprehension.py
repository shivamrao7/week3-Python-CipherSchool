# squares = []
# # for i in range(1,11):
# #     squares.append(i**2)
# # print(squares)

# square2 = [i**2 for i in range(1,11)]
# print(square2)

# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)
# # same
# new_negative = [-i for i in range(1,11)]

names = ['Harshit', 'Mohit', "rohit"]
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)

#   same

new1_list = [name[0] for name in names]
print(new1_list)