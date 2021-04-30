def bubble_sort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

a=[8,2,3,0,9,6,1]
b=bubble_sort(a)
print(b)
