def solution(participant, completion):
    dic = {}

    # 참가자 수 세기
    for p in participant:
        dic[p] = dic.get(p, 0) + 1

    # 완주자 제거
    for c in completion:
        dic[c] -= 1

    # 0이 아닌 사람 찾기
    for key in dic:
        if dic[key] != 0:
            return key
