#You are given four integers 'a', 'b', 'y' and 'x', where 'x' can only be either zero or one. Your task is as follows: 
#
#If 'x' is zero assign value 'a' to the variable 'y', if 'x' is one assign value 'b' to the variable 'y'. 
#
#You are not allowed to use any conditional operator (including ternary operator). 
#Follow up: Solve the problem without utilizing arithmetic operators '+ - * /'.


#    int arr[2];
#    arr[0] = a;
#    arr[1] = b;
#    y = arr[x];

def give_value(a, b, x):
    y = 0 
    while b > 0:
        y <<= 1
        y |= (b&x)
        b >>= 1 


    x ^= 1 
     
    while a > 0:
        y <<= 1
        y |= (a&x)
        a >>= 1 

    return y

if __name__ == "__main__":
    print give_value(1, 2, 0)
    print give_value(1, 2, 1)
