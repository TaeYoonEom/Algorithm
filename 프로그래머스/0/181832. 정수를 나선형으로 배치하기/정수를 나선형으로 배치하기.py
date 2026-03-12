def solution(n):
    
    arr = [[0]*n for _ in range(n)]
    
    dx = [0,1,0,-1]   # → ↓ ← ↑
    dy = [1,0,-1,0]
    
    x,y = 0,0
    direction = 0
    
    for num in range(1, n*n+1):
        arr[x][y] = num
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if nx<0 or ny<0 or nx>=n or ny>=n or arr[nx][ny] != 0:
            direction = (direction+1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
            
        x,y = nx,ny
    
    return arr