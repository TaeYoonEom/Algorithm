def solution(a, b):
    concat_val = int(str(a) + str(b))
    mult_val = 2 * a * b
    
    return max(concat_val, mult_val)
