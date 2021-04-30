def bubble_sort(arr):
    for i in range(len(arr)-1):

        for j in range(len(arr)-i-1):           #for every iteration 1 element is sorted for ith iteration i numbers are sorted 
                                                #Therefore we minus i and sort remaining numbers           
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr   

a=[5,4,3,2,1]
b = bubble_sort(a)
print(b)    
