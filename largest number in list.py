num = int(input('How many numbers: '))
lst = []
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print("Maximum element in the list is :", max(lst))

# using sort
list1 = [10, 20, 4, 45, 99]

list1.sort()

print("Largest element is:", list1[-1])

# using max function
list1 = [10, 20, 4, 45, 99]

print("Largest element is:", max(list1))
