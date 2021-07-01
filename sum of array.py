# 1.Sum of array using sum function

arr = [12, 3, 4, 15]

ans = sum(arr)

print('Sum of the array is ', ans)


# 2.using function

def _sum(arr):

    sum=0

    for i in arr:
        sum = sum + i

    return(sum)

arr=[]

arr = [1,2,3,4,5,6,7,]

n = len(arr)

ans = _sum(arr)

print ('Sum of the array is ', ans)