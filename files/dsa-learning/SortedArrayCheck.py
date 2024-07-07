def is_array_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True


l1 = [1,2,3,4,5,6,6,6,-1,6]

print(is_array_sorted(l1))
