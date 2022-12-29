nums = [1,2,3,4,5,6,7,8,9,10]
new_list = [-1,2,-3,8]

new_list = []
for i in nums:
    if i%2 ==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)
# if else both sath me use karne ho to ham starting me likhe ge if else ko
nw_list2 = [i*2 if (i%2==0) else -i for i in nums]
print(nw_list2)