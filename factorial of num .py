'''my_num = int(input("Enter a number :"))
my_factorial = 1
while(my_num>0):
   my_factorial = my_factorial*my_num
   my_num=my_num-1
print("The factorial of the number is : ")
print(my_factorial''')

def count_words():
   file = open("article.txt", "r")
   count = 0
   for line in file:
      words = line.split()
      for word in words:
         if word[-1] == 'e':
            count += 1
   print(count)


count_words()

