def solution(triangle):
    tmp = 0
    rst = 0
    DP = int(triangle[0][0])
    # DP[i][j] = DP[i-1][j-1] + DP[i-1][j] + A[i][j]
    for i in range(1, len(triangle)):
        DP += rst
        tmp = 0
        rst = 0
        for j in range(1, len(triangle[i])):
            tmp = max(triangle[i][j], triangle[i][j - 1])
            if tmp > rst:
                rst = tmp

    print(DP)

    return DP

b = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
a = solution(b)