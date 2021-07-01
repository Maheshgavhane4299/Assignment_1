# using slicing

list1 = [10, 20, 4, 45, 99]
list1.sort()

print("Smallest element is:", *list1[:1])

#  maximum element using min function
list1 = [10, 20, 1, 45, 99]


print("Smallest element is:", min(list1))

#
list1 = []

num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

print("Smallest element is:", min(list1))
