def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        # 응급도보다 더 높은 값이 몇 개인지 세어서 순위 계산
        count = 1
        for j in range(len(emergency)):
            if emergency[j] > emergency[i]:
                count += 1
        answer.append(count)
    return answer
