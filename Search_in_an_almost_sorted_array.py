import pdb
def binarySearch(arr, l, r, target):
    
    while l <= r:
        mid = l + (r - l)/2
        #print mid       

        #pdb.set_trace()

        if mid - 1 >= 0 and arr[mid - 1] == target:
            return mid - 1
   
        if mid + 1 <= r and arr[mid + 1] == target:
            return mid + 1

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1


if __name__ == "__main__":
    arr = [10, 3, 40, 20, 50, 80, 70]
    print binarySearch(arr, 0, len(arr) - 1, 80)
