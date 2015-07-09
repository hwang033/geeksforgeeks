import pdb

def build_expressrion(nums, expression):
    #T(n) = (4*n^2)T(n-1) + 4n^2
    if len(nums) == 1 and nums[0] == '24':
        return expression 
    
    if len(nums) == 1:
        return None 

    for i in range(len(nums)):
        val_i = nums[i] 
        e_i = expression[i]
        for j in range(len(nums)):
            if i == j:
                continue
            val_j = nums[j]
            e_j = expression[j]
            
            for e in ['+', '-', '*', '/']:
                if e == '/' and val_j == '0': 
                    continue
                rst = eval(val_i + e + val_j) 
                new_nums = nums[:]
                new_expression = expression[:]
                if j > i:
                    i, j = j, i
                new_nums.pop(i)
                new_nums.pop(j)
                new_nums.append(str(rst))

                new_expression.pop(i)
                new_expression.pop(j)
                new_expression.append('(%s)' %(e_i + e + e_j))
                new_expression = build_expressrion(new_nums,\
                                                   new_expression)
                if new_expression is not None: 
                    return new_expression 
    return None   


if __name__ == "__main__":
    print build_expressrion(['30', '2', '2', '8'], ['30', '2', '2', '8'])
