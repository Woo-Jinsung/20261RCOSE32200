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

#3
from collections import deque

def solution(v1, v2, a, b):
    answer = 0
    size = 1001
    graph = [[] for _ in range(size)]
    visited = [False] * size
    n = len(v1)

    for i in range(n):
        x = v1[i]
        y = v2[i]
        graph[x].append(y)
        graph[y].append(x)
    
    def bfs(start, end):
        visited[start] = True
        cand = []
        queue = deque()
        count = 0
        queue.append((start, count))
        while queue:
            now, cnt = queue.popleft()
            if cnt >= 2:
                continue

            for v in graph[now]:
                if visited[v] == False:
                    if v == end and cnt == 1:
                        cand.append(now)
                    else:
                        visited[v] = True
                        queue.append((v, cnt + 1))
        return cand
    
    cand = bfs(a, b)
    if len(cand) == 0:
        return -1
    
    minimum = float('inf')

    for c in cand:
        temp = len(graph[c])
        if minimum > temp:
            minimum = temp
            answer = c
    
    return answer