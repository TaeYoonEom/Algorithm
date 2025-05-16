s = input()
for c in s:
    if 'a' <= c <= 'z':
        print(chr(ord(c) - 32), end='')
    elif 'A' <= c <= 'Z':
        print(chr(ord(c) + 32), end='')
    else:
        print(c, end='')
