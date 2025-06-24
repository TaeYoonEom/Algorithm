def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        temp = word
        for p in possible:
            temp = temp.replace(p, ' ')
        # 모두 제거 후 공백만 남았는지 확인
        if temp.strip() == '':
            # 중복 발음이 없는지 확인
            if all(word.count(p) <= 1 for p in possible):
                answer += 1
    return answer
