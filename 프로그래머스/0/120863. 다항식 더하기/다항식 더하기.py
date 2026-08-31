def solution(polynomial):
    new_poly = polynomial.split(" + ")
    x_coef = 0
    c = 0
    
    for term in new_poly:
        if "x" in term:
            term = term.replace("x", "")
            x_coef += int(term) if len(term) > 0 else 1
        else:
            c += int(term)
    
    poly_result = []
    if x_coef > 0:
        poly_result.append("x" if x_coef==1 else f"{x_coef}x")
    
    if c > 0:
        poly_result.append(str(c))
    
    return " + ".join(poly_result)