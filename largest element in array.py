def largest(arr, n):
    # Initialize maximum element
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [50,100,40,200,500]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array is", Ans)