# # opwn file and write something
# f=open("abc.txt",'w')
# f.write("priyanka\n")
# f.write("Mahesh\n")
# f.write("Gavhane\n")
# print("Data written to the file successfully")
# f.close()

# to read all data from file
# f=open("abc.txt",'r')
# data = f.read()
# print(data)
# f.close()

# to read only first 10 char
# f=open("abc.txt",'r')
# data = f.read(10)
# print(data)
# f.close()

# to read data line by line

# f = open ("abc.txt",'r')
# line1 = f.readline()
# print(line1,end="")
# line2 = f.readline()
# print(line2,end="")
# line3 = f.readline()
# print(line3,end="")
# f.close()

# to read all llines into list
#
# f = open("abc.txt",'r')
# lines = f.readlines()
# for line in lines:
#     print(line ,end ="")
# f.close()

# f =open ("abc.txt",'r')
# print(f.read(3))
# print(f.readline())
# print(f.read(4))
# print("remaining data")
# print(f.read())

# the with statement

# with open("abc.txt","w") as f:
#     f.write("Durga\n")
#     f.write("Software\n")
#     f.write("Solutions\n")
#     print("Is File Closed: ",f.closed)
# print("Is File Closed: ",f.closed)

# tell() function use to find current position of pointer

# f=open("abc.txt","r")
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# print(f.read(3))
# print(f.tell())
#
# # to jump to a specified position
#
# data="team brainworks solution "
# f=open("abc.txt","w")
# f.write(data)
# with open("abc.txt","r+") as f:
#     text=f.read()
#     print(text)
#     print("The Current Cursor Position: ",f.tell())
#     f.seek(16)
#     print("The Current Cursor Position: ",f.tell())
#     f.write("classess")
#     f.seek(0)
#     text=f.read()
#     print("Data After Modification:")
#     print(text)

# import os,sys
# fname = input (" enter file name:")
# if os.path.isfile(fname):
#     print("file exists:",fname)
#     f = open(fname,'r')
# else:
#     print("file does not exists:",fname)
#     sys.exit(0)
# print("the content of file:")
# data = f.read()
# print(data)

# print the no of lines,words,character present in given file

import os,sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exist:",fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
print("The number of Lines:",lcount)
print("The number of Words:",wcount)
print("The number of Characters:",ccount)