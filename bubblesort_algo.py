# bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if (arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
        #print(arr)
    return arr



#main
my_list = [4,2,1,6,3,7,8,5,9]
print("orignial list before:", my_list)
bubble_sort(my_list)
print("sorted list:", my_list)