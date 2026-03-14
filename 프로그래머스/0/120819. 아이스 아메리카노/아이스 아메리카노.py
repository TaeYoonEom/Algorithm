def solution(money):
    
    coffee = money // 5500
    moneys = money % 5500
    
    return [coffee, moneys]