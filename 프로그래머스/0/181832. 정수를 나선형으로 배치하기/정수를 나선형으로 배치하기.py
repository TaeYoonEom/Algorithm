def solution(n):
    # 1. n x n 배열 생성 (0으로 초기화)
    board = [[0] * n for _ in range(n)]
    
    # 2. 방향: 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]  # 행 이동
    dy = [1, 0, -1, 0]  # 열 이동
    
    x, y, direction = 0, 0, 0  # 시작 위치 및 방향
    num = 1  # 채울 숫자

    for _ in range(n * n):
        board[x][y] = num
        num += 1
        
        # 다음 위치 계산
        nx, ny = x + dx[direction], y + dy[direction]
        
        # 조건 확인: 범위 내 && 아직 안 채운 곳
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            x, y = nx, ny
        else:
            # 방향 전환
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]
    
    return board
