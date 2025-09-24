a = [4, 10, 15, 18, 19]
i = 0
sm = 0
flag = True
while flag:
    num = a[i]
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            break
    else:
        flag = False
    if not flag:
        continue
    sm += num
    i+=1
print(sm, sum(a[:-1]))
