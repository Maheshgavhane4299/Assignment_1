#
start, end = -5, 5

for num in range(start, end + 1):

    if num < 0:
        print(num, end=" ")
#

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):

    if num < 0:
        print(num, end=" ")