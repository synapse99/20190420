s = 0
even_s = 0
odd_s = 0
sevn_s = 0

i = 1

while i <= 100:
    s += i

    if i % 2 ==0:
        even_s += i
    else:
        odd_s += i

    if i % 7 ==0:
        sevn_s += i


    i +=1


print("1부터 100까지의 합 = ",s)
print("1부터 100까지의 홀수들의 합 =",odd_s)
print("1부터 100까지의 짝수들의 합 =", even_s)
print("1부터 100까지의 7의 배수들의 합 =", sevn_s)
