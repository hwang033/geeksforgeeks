import pdb
def print_permutations(string, idx):
    
    if idx == len(string):
        print ''.join(string)

    for i in range(idx, len(string)):
        #pdb.set_trace()
        print_permutations( string[0:idx] + [string[i]] + string[idx:i] + string[i+1:], idx + 1)

if __name__ == "__main__":
    print_permutations(['a', 'b', 'c', 'd'], 0)
        
        
    
