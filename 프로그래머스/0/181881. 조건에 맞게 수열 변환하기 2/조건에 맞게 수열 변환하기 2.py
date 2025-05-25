def solution(arr):
    x = 0

    while True:
        changed = False
        new_arr = arr[:]

        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                new_arr[i] = arr[i] // 2
                if new_arr[i] != arr[i]:
                    changed = True
            elif arr[i] < 50 and arr[i] % 2 == 1:
                new_arr[i] = arr[i] * 2 + 1
                if new_arr[i] != arr[i]:
                    changed = True

        if not changed:
            break

        arr = new_arr
        x += 1

    return x
