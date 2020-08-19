def _sum(stack, p, n):
    j = n - 1
    sum_of_top_elements = 0
    while p:
        sum_of_top_elements += stack[j]
        j -= 1
        p -= 1
    return sum_of_top_elements

def solution(stack, K):
    dp = [[0]*(len(s) + 1) for s in stack]
    for k in range(K):
        dp[0][k] = _sum(stack[0], k, len(stack[0]))

    for i in range(1, len(stack)):
        for k in range(1, K + 1):
            dp[i][k] = dp[i - 1][k]
            for j in range(1, K + 1):
                if len(stack[i]) >= j:
                    dp[i][k] = max(
                        dp[i][k],
                        dp[i - 1][k - j] + _sum(stack[i], j, len(stack[i])))
    return dp[-1][K]


print(solution([[1,1,100,3],[2000,2,3,1],[2,10,1,4]], 3))
