#Given a sorted array, remove the duplicat elements


#first approach is using extra space, a list
def remove_duplicates(arr):
    result = []
    if len(arr) == 1:
        result.append(arr[0])
        return result
    else:
        result.append(arr[0])
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                result.append(arr[i])

    return result


#efficient solution to do in-place swapping

def remove_duplicates_(arr):
    if len(arr) == 1:
        return len(arr)
    else:
        ptr = 0
        for i in range(1, len(arr)):
            if arr[i] != arr[ptr]:
                ptr += 1
                arr[ptr] = arr[i]

        return arr[:ptr+1]


l2 = remove_duplicates_([1, 2, 3, 3, 5, 5, 7, 8, 8, 10])
print(l2)
