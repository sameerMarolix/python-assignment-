
def insersionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        print(arr)
        arr[j+1] = key
        print(arr)

un_list = [64,25,12,22,11]
insersionSort(un_list)
print(un_list)