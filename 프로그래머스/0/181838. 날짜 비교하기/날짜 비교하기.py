from datetime import datetime

def solution(date1, date2):
    answer = 0
    
    datetime1 = datetime(date1[0], date1[1], date1[2])
    datetime2 = datetime(date2[0], date2[1], date2[2])
    
    if datetime1 < datetime2:
        return 1
    else:
        return 0