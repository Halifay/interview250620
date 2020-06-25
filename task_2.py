# 1
f = open("names.txt", "r")
names = (f.read()).replace("\"", "").split(",")
names.sort()

# 2
alp_sum = []
for i in range(len(names)):
    s = 0
    for char in names[i]:
        s += (ord(char) - ord('A') + 1)
    alp_sum.append(s)

# 3
mult_sum = []
for i in range(len(names)):
    mult_sum.append(alp_sum[i]*(i+1))

# 4
answer = sum(mult_sum)
print(answer)
# ответ 871853874

