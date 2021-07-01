# using for loop
list1 = [11, 5, 17, 18, 23]

total =0

for ele in range(0, len(list1)):
    total = total + list1[ele]

print("Sum of all elements in given list: ", total)


# using sum function

list1 = [11, 5, 17, 18, 23]

# using sum() function
total = sum(list1)

# printing total value
print("Sum of all elements in given list: ", total)