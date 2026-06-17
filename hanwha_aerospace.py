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

