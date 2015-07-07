# given an array and is rotated n number of times find the number where the peak happens. The array is sorted in increasing order. how will you rearrange them in normal sorted order
# find peak algorithm is learned from school


def find_peak(array):
   
    low = 0
    high = len(array) - 1

    while low < high:
        mid = low + (high - low)/2
        if array[mid] < array[low]:
            high = mid - 1
        else:
            low = mid
    
    return low


if __name__ == "__main__":
    # rearrage them can using reverse [0:pivot], [pivot:], then reverse [:]
    arr = [4, 7, 9, 12, 1, 2]
    p = find_peak(arr)
    arr1 = arr[:p + 1][::-1] + arr[p+1:][::-1]
    print arr1[::-1]
     
