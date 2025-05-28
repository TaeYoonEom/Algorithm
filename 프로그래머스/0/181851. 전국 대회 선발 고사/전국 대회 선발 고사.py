def solution(rank, attendance):
    # 출석한 학생들의 인덱스만 필터링
    candidates = [i for i in range(len(attendance)) if attendance[i]]

    # 출석한 학생들 중에서 등수가 낮은 순서대로 정렬
    top3 = sorted(candidates, key=lambda i: rank[i])[:3]

    # 인덱스 a, b, c 추출
    a, b, c = top3

    # 계산
    return 10000 * a + 100 * b + c
