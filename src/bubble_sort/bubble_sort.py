def bubble_sort(array):
    
    arr_length = len(array)
    for i in range(0,arr_length-1):
        for j in range(0,arr_length-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
                
    
