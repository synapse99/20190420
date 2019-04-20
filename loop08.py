s = 0
i = 1


while i <= 100:
    s += i
    if(s >= 1000):
        break
    i += 1
print("최초로 합이 1000을 넘는 i값고 그 합은 ",i, s)
