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

#3
def solution(category, relation, member, article):
    answer = [0] * len(article)
    dict_r = {}
    arr = []
    def findchild(target):
        nonlocal dict_r, arr
        if dict_r.get(target, 0) == 0:
            arr.append(target)
            return
        else:
            for i in dict_r[target]:
                arr.append(i)
                findchild(i)
    
    for relate in relation:
        parent, child = relate.split()
        if dict_r.get(parent, 0) == 0:
            dict_r[parent] = [child]
        else:
            dict_r[parent].append(child)
    
    for cate in category:
        if dict_r.get(cate, 0) == 0:
            dict_r[cate] = 0
    
    for mem in member:
        mem = list(mem.split())
        person = mem[0]
        targets = mem[1:]
        arr = []
        for target in targets:
            if target in arr:
                continue
            else:
                arr.append(target)
                findchild(target)
        
        for i, art in enumerate(article):
            available = False
            art = list(art.split())
            for a in art:
                if a in arr:
                    available = True
                    break
                if available:
                    answer[i] += 1
    
    return answer