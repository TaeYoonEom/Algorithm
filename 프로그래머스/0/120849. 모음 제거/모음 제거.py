def solution(my_string):
    vowels = 'aeiou'
    result = ''
    for char in my_string:
        if char not in vowels:
            result += char
    return result
