def solution(id_list, report, k):
    answer = []
    N = len(id_list)
    report_graph = [set() for _ in range(N)]
    mail_count = [0] * N
    
    for r in report:
        reporter, reported = r.split()
        reporter_idx = id_list.index(reporter)
        reported_idx = id_list.index(reported)
        report_graph[reported_idx].add(reporter_idx)
    
    
    for j in range(N):
        if len(report_graph[j]) >= k:
            for reporter in report_graph[j]:
                mail_count[reporter] += 1
    
    return mail_count