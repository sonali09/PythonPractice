def bubbleSrtPrac(arr):
    n=len(arr)
    for i in range(0, n-1):
        flag=0
        for j in range(0, n-1-i):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1]= temp
                flag =1        
        if(flag==0):
            break
    return arr

arr = [2,4,65,43,21,55,55,2,62,52,22,7,9]
arr1=bubbleSrtPrac(arr)
print(arr1)
    