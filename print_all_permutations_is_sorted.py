import pdb
def print_permutations(string, idx):# T(n) = nT(n-1) + o(n^2)= O(n!) + (N * (N + 1) * (2N + 1)) / 6 = O(n!) + O(n^3) = O(n!)
    
    if idx == len(string):
        print ''.join(string)

    for i in range(idx, len(string)):
        #pdb.set_trace()
        print_permutations(string[0:idx] + [string[i]] + string[idx:i] + string[i+1:], idx + 1)

if __name__ == "__main__":
    print_permutations(['a', 'b', 'b', 'd'], 0)
        
        
    
