def count_decoding_num(digits):
    
    if len(digits) <= 1:
        return 1
    with_n1 = 0
    with_n1n2 = 0
    n1 = digits[0] 
    n2 = digits[1]
    with_n1 += count_decoding_num(digits[1:])
    if n1*10 + n2 <= 26: 
        with_n1n2 += count_decoding_num(digits[2:]) 
    return with_n1 + with_n1n2    

def count_decoding_num2(digits):
# f[i] = 1 + f[i+1] #if d[i]*10 + d[i +1] < 26
    f = [0 for i in digits]
    f[-1] = 1
    for i in range(len(digits)-2, -1, -1):
        if digits[i]*10 + digits[i-1] <= 26: 
            f[i] = 1 + f[i+1]
        else:
            f[i] = f[i+1]

    return f[0]


if __name__ == "__main__":
    print count_decoding_num2([1,2,1])
    print count_decoding_num2([1,2,3,4])
