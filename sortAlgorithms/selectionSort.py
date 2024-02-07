

def selectionSort(arr):
    for i in range(len(arr)):
        minInd = i
        for j in range(i+1,len(arr)):
            if arr[minInd]>arr[j]:
                minInd = j
        arr[i],arr[minInd] = arr[minInd],arr[i]


un_list = [64,25,12,22,11]
selectionSort(un_list)
print(un_list)
