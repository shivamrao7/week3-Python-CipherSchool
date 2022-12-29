numbers = list(range(1,11))
print(numbers)
even_nums = []
for i in numbers:
    if i%2==0:
        even_nums.append(i)
print(even_nums)

even_nums = [i for i in numbers if i%2 == 0]
even_nums2 = [i for i in range(1,11) if i%2==0]

odd_nums = [i for i in range(1,11) if i%2!=0]
print(odd_nums)