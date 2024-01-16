def bubleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print(arr)
    #return arr

un_list = [64,25,12,22,11]
bubleSort(un_list)
print(un_list)
