# using for loop

list1 = [10, 21, 4, 45, 66, 93]

for num in list1:

    if num % 2 == 0:
        print(num, end=" ")

#  using list comprehension
list1 = [10, 21, 4, 45, 66, 93]


even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list: ", even_nos)

 # we can also print even no's using lambda exp.
list1 = [10, 21, 4, 45, 66, 93, 11]

even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list: ", even_nos) 