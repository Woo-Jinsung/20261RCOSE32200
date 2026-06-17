#한화시스템/방산 260425
#Python3으로 총 3문제 120분

#1
def solution(fishes, feeds):
    fishes.sort(reverse=True)
    n = len(feeds)
    for i in range(n):
        feed = feeds[i]
        for fish in fishes:
            if fish <= feed:
                feed -= fish
            else:
                fishes.pop()

    return len(fishes)

#2
def solution(square, k):
    dp = [[] for _ in range(11)]
    dp[1] = square
    now = 1
    while now <= k:
        start = [row.copy() for row in dp[now]]
        n = len(start)
        temp = [[] * (2 * n) for _ in range(2 * n)]

        for i in range(n):
            temp[i] = start[i]
            for j in range(n - 1, -1, -1):
                temp[i].append(start[i][j])
            temp[2 * n - i - 1] = temp[i]
        
        now += 1
        dp[now] = temp
    
    return dp[k + 1]

