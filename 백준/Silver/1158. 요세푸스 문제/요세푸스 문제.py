N, K = map(int, input().split())

num_list = [i+1 for i in range(N)]
sorted_list = []
loc = 0

while(num_list):
    loc = (loc+K-1)%len(num_list)
    temp = num_list[loc]
    sorted_list.append(temp)
    del num_list[loc]
print("<", end="")
print(*sorted_list, sep=", ", end="")
print(">")