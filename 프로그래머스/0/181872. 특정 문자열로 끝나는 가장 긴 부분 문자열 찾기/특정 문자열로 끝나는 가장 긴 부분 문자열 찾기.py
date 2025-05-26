def solution(myString, pat):
    idx = myString.rfind(pat)  # pat이 마지막으로 등장하는 인덱스
    if idx != -1:
        return myString[:idx + len(pat)]
    return ""
