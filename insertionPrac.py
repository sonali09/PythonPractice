def insertSrt(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j=i-1
        while (j >=0 and arr[j]> temp):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    return arr

arr = [2,4,65,43,21,55,55,2,62,52,22,7,9]
arr1=insertSrt(arr)
print(arr1)