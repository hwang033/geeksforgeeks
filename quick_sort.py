import pdb
def partition(arr, l, h):

    pivot = arr[h]
    j = -1
    for i in range(l , h):
        if arr[i] > pivot and j == -1:
            j = i
        elif arr[i] < pivot and j != -1:
           arr[i], arr[j] = arr[j], arr[i] 
           j += 1
   
    if j != -1:
        arr[h], arr[j] = arr[j], arr[h] 
        return j

    return h

def quick_sort(arr, s, e):
    if s >= e: 
        return 

    p = partition(arr, s, e)
    #print arr, s, p - 1, p + 1, e
    #pdb.set_trace()

    quick_sort(arr, s, p - 1)
    quick_sort(arr, p + 1, e) 


if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1, 2, 7, 8]
    quick_sort(arr, 0, len(arr) - 1)
    print arr
    
