from itertools import permutations

def solution(spell, dic):
    # spell의 모든 문자를 나열한 순열 생성
    sums = ["".join(p) for p in permutations(spell, len(spell))]

    # dic 안에 존재하는지 확인
    for word in sums:
        if word in dic:
            return 1
    return 2
