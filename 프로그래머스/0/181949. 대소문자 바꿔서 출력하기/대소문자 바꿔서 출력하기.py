text = input()
result = ''

for ch in text:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch  # 공백이나 숫자 같은 건 그대로 추가

print(result)
