def insertionSort(a):
    n=len(a)
    #we assume first element is already sorted hence comaparision starts from 1st element
    for i in range(1,n):
        # cval=a[i]
        pos=i
        # position must be greater than 0 and position-1 element must be greater than its right element i.e. position element(cval)
        while pos>0 and a[pos-1]>a[pos]:
            a[pos],a[pos-1]=a[pos-1],a[pos]
            pos-=1
        # a[pos]=cval
l=[5,2,-1,0,10]
insertionSort(l)
print(l)