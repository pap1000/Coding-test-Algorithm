N = int(input())
Wanted = 666
count = 0

while True:
    if '666' in str(Wanted):
        count += 1
        if count == N:
            print(Wanted)
            break
    Wanted += 1