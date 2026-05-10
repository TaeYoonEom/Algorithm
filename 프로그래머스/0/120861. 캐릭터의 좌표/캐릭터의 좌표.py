def solution(keyinput, board):
    answer = [0, 0]
    maxsize1 = board[0] // 2
    maxsize2 = board[1] // 2
    
    for i in range(len(keyinput)):
        if keyinput[i] == 'left':
            if -maxsize1 < answer[0]:
                answer[0] -= 1
        elif keyinput[i] == 'right':
            if maxsize1 > answer[0]:
                answer[0] += 1
            
        if keyinput[i] == 'up':
            if maxsize2 > answer[1]:
                answer[1] += 1
        elif keyinput[i] == 'down':
            if -maxsize2 < answer[1]:
                answer[1] -= 1
            
    return answer