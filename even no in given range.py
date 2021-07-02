# Python program to print Even Numbers in given range

start, end = 4, 19

for num in range(start, end + 1):

    if num % 2 == 0:
        print(num, end=" ")

# input from keyboard

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):

    if num % 2 == 0:
        print(num, end=" ")