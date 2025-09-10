def solution(polynomial):
    terms = polynomial.split(' + ')
    x_sum = 0
    const_sum = 0

    for term in terms:
        if 'x' in term:
            coeff = term.replace('x', '')
            x_sum += int(coeff) if coeff else 1
        else:
            const_sum += int(term)
    
    result = []
    
    if x_sum:
        result.append(f"{x_sum}x" if x_sum > 1 else "x")
        
    if const_sum:
        result.append(str(const_sum))
    
    return ' + '.join(result)