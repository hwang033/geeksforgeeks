class Solution:
    # @param {integer} n
    # @return {integer}

        
    def numTrees(self, n):
        #cantalan number
        if n == 0:
            return 0
        rst = self.combination(2*n, n)
        return rst/(n+1)
        
    def combination(self, n, k):
        
        if k > n:
            return 0
        if k > n - k:
            k = n - k 
        
        res = 1
        
        for i in range(k):
            res *= n - i
            res /= i + 1
        return res

if __name__ == "__main__":
    s = Solution()
    print s.numTrees(2)
