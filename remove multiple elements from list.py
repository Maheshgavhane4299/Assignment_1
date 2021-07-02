list = [1,2,3,4,5,10,15,20,25]
for num in list:
    if num %2 ==0:
        print(num,end =' ')

#using remove function
list = [1,2,3,4,5,10,15,20,25,27,30]

for num in list :

    if num % 2 !=0:
        list.remove(num)

print (list)

#using del keyword

list1 = [11, 5, 17, 18, 23, 50]

del list1[1:5]

print(*list1)