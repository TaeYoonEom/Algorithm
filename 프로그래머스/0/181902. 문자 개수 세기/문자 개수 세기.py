def solution(my_string):
    answer = [0] * 52  # A-Z: 0~25, a-z: 26~51

    for char in my_string:
        if 'A' <= char <= 'Z':
            answer[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':
            answer[ord(char) - ord('a') + 26] += 1

    return answer
