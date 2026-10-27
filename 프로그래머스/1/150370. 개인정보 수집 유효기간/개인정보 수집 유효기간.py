def solution(today, terms, privacies):
    answer = []
    year, month, day = today.split(".")
    todays = 336 * int(year) + 28 * (int(month) - 1) + int(day)
    
    terms_dic = {}
    for item in terms:
        term, duration = item.split()
        terms_dic[term] = 28 * int(duration)
    
    for i, privacy in enumerate(privacies):
        p, p_term = privacy.split()
        p_year, p_month, p_day = p.split(".")
        p_days = 336 * int(p_year) + 28 * (int(p_month) - 1) + int(p_day)
        if todays - p_days >= terms_dic[p_term]:
            answer.append(i + 1)
    
    return answer