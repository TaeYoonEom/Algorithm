def solution(phone_number):
    answer = ''
    lens = len(phone_number) - 4
    return lens * "*" +phone_number[-4:]
