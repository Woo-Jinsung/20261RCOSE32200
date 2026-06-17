#한화에어로스페이스 0419
#Python3으로 총 4문제 120분

#1
def solution(n, k, menu):
    ans = []
    for i in range(n):
        temp = menu[i][0] * 4 + menu[i][1] * 4 + menu[i][2] * 9
        ans.append(temp)
    
    ans.sort()
    return sum(ans[:k])

#2
def findlog(num):
    ans = 0
    while num >= 10:
        num = num // 10
        ans += 1
    return ans

def solution(initdb, mindb, maxdb, commands):
    answer = []
    now = initdb
    for command in commands:
        if command[0] == 0:
            target = findlog(command[1]) * 10
            if now + target >= maxdb:
                now = maxdb
            else:
                now += target
        elif command[0] == 1:
            target = findlog(command[1]) * 10
            if now - target <= mindb:
                now = mindb
            else:
                now -= target
        elif command[0] == 2:
            if now + command[1] >= maxdb:
                now = maxdb
            else:
                now += command[1]
        elif command[0] == 3:
            if now - command[1] <= mindb:
                now = mindb
            else:
                now -= command[1]
        
        answer.append(now)
    
    return answer