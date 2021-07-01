# list = [1,2,3,4,5,6,7,8]
# list2 = list.copy()
# print(list2)


#list comprehension
def Cloning(li1):
    li_copy = [i for i in li1]
    return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)