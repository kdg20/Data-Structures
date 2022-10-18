def binarySearch(Arr,ele):
    low,high=0,len(Arr)-1
    while low<=high:
        mid=(low+high)//2
        if Arr[mid]==ele:
            return mid
        elif ele<Arr[mid]:
            high=mid-1
        elif ele>Arr[mid]:
            low=mid+1
l=[1,2,3,4,5,6]
index=binarySearch(l,6)
print("Number found at index ->",index)
