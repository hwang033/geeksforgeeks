
i = 0

def print_conbinations(arr, r, idx, rst):
# T(n) = 2T(n-1) + o(1) the function run r time so the value is n^r
    global i
    i += 1

    if len(rst) == r:
        print rst
        return 

    #don't choose idx th element
    if r - len(rst) <= len(arr) - idx - 1:
        print_conbinations(arr, r, idx+1, rst[:])

    #choose idx th element
    rst.append(arr[idx])

    if r - len(rst) <= len(arr) - idx - 1:
        print_conbinations(arr, r, idx+1, rst[:])


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    r = 5
    idx = 0
    rst = []
    print_conbinations(arr, r, idx, rst)
    print "i=%d" %i  
