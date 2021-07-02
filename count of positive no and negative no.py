# count pos,neg no in given list

list1 = [-1,-10,20,-4,-8,10, 21, 4, 45, 66, 93, 1]

pos_count, neg_count = 0, 0

for num in list1:

    if num >= 0:
        pos_count += 1

    else:
        neg_count += 1

print("Even numbers in the list: ", pos_count)
print("Odd numbers in the list: ", neg_count)

# count pos,neg no in given list

list1 = [-1,-10,20,-4,-8,10, 21, 4, 45, 66, 93, 1]

pos_count = len(list(filter(lambda x: (x >= 0), list1)))

neg_count = len(list(filter(lambda x: (x < 0), list1)))

print("pos numbers in the list: ", pos_count)
print("neg numbers in the list: ", neg_count)