list = [10,20,30,-40,15,-20]

for num in list:
    if num >=0:
        print(num ,end =" ")

#using list comprehension
list1 = [-10, -21, -4, 45, -66, 93]


pos_nos = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", *pos_nos)