#한화에어로스페이스 0329
#Python3으로 총 5문제 180분

#1
def solution(n, m, features):
    answers = []
    for feature in features:
        answers.append(feature[0] * n + feature[1] * m)
    answers.sort()
    return answers[0]