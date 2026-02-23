dwarfs = [int(input()) for _ in range(9)]
true_dwarfs = []
total_sum = sum(dwarfs)
for i in range(9):
    for k in range(i+1,9):
        if total_sum - dwarfs[i] - dwarfs[k] == 100:
            true_dwarfs = [val for idx, val in enumerate(dwarfs) if idx not in {i, k}]
            break
        if true_dwarfs:
            break
true_dwarfs.sort()
print(*true_dwarfs, sep = '\n')