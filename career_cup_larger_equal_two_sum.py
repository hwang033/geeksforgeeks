#given a sorted array and n, find the count of sum of 2 numbers greater than or equal to n

def two_sum(arr, target):
    low = 0
    high = len(arr) - 1
    cnt = 0

    while low < high:
        sum_v = arr[low] + arr[high] 
        if sum_v >= target:
            # if sum value contains high 
            cnt += high - low
            high -= 1
        else:    
            low += 1
   
    return cnt

if __name__ == "__main__":
    print two_sum([1, 5, 7, 9, 30, 33, 35, 65, 67], 42)
    print 8 + 7 + 4 + 2
