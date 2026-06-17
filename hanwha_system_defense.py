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