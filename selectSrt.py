def selectSrt(arr):
    n= len(arr)
    for i in range(0,n):
        min = i
        for j in range(i+1, n):
            if(arr[i]> arr[j]):
                min = j
        if(min != i):
            temp=arr[i]
            arr[i]= arr[min]
            arr[min]=temp
    return arr

arr = [2,4,65,43,21,55,55,2,62,52,22,7,9]
arr1=selectSrt(arr)
print(arr1)