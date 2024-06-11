def bubbleSort(arr,reverse=False):
    #[2,4,3,6,8,4,5]
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if reverse:
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]

            else:
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]


    return arr
print(bubbleSort([2,4,3,6,8,4,3,4,5,199,345,5],reverse=True))


