def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    

def merge(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    
    i = j = 0
    arrInd = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[arrInd] = left[i]
            i += 1
        else:
            arr[arrInd] = right[j]
            j += 1
        arrInd += 1    

    while i < len(left):
        arr[arrInd] = left[i]
        i += 1
        arrInd += 1

    while j < len(right):
        arr[arrInd] = right[j]
        j += 1
        arrInd += 1
