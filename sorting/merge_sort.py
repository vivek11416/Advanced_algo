def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge_two_sorted_list(sortedLeft, sortedRight)


def merge_two_sorted_list(arr1,arr2):
    sortedList = []
    i,j=0,0

    while i<len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sortedList.append(arr1[i])
            i+=1

        else:
            sortedList.append(arr2[j])
            j += 1

    sortedList.extend(arr1[i:])
    sortedList.extend(arr2[j:])
    return sortedList


print(mergeSort([2,4,2,6,8,3,45,1,1]))
#print(merge_two_sorted_list([5,8,12,56,89,100],[7,9,45,51]))