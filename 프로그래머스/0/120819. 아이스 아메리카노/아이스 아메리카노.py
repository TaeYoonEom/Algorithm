def solution(money):
    answer = []
    icecoffee = 5500
    count = 0
    
    while(money >= icecoffee):
        money -= icecoffee
        count += 1
        
    answer += (count, money)
    return answer