def selectionSort(arr):
    n=len(arr)
    # it will iterate for n-1 times
    for i in range(n-1):
        position=i
        # it will iterate from next element of i to n
        for j in range(i+1,n):
            if arr[j]<arr[position]:
                position=j
        # swapping
        arr[i],arr[position]=arr[position],arr[i]
    return arr
arr=[3,5,4,1,0]
result=selectionSort(arr)
print(result)