def solution(clothes):

    dict_clothes = {}
    for val, key in clothes:
        if key in dict_clothes.keys():
            dict_clothes[key] += 1
        else:
            dict_clothes.update({key : 1})

    answer = 1
    for val_cnt in dict_clothes.values():
        answer *= val_cnt + 1

    return answer - 1