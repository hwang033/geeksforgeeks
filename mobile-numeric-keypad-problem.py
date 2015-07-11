
keyboard = [[1,2,3],
            [4,5,6],
            [7,8,9],
            [-1,0,-1]]


def count(n):
    f = [[0 for j in range(10)] for i in range(n)]
    f[0] = [1 for j in range(10)]

    for i in range(1, n):
        for j in range(10):
            row, col = (3, 1) if j == 0 else divmod(j-1, 3) 
            for nrow, ncol in [(row+1, col),(row-1, col)\
                               ,(row, col),(row, col-1),(row, col+1)]: 
                if 0 <= nrow <= 3 and 0 <= ncol <= 2:
                    former = keyboard[nrow][ncol]
                    if former != -1:
                        f[i][j] += f[i-1][former]
    print sum(f[-1])

if __name__ == "__main__":
    count(1)
    count(2)
    count(3)
    count(4)
