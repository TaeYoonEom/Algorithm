def solution(chicken):
    service = 0
    coupon = chicken

    while coupon >= 10:
        new = coupon // 10       # 새로 받는 서비스 치킨
        service += new           # 서비스 치킨 누적
        coupon = new + coupon % 10  # 서비스 치킨에서 나온 쿠폰 + 나머지 쿠폰
    
    return service
