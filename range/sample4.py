# 判断质数

l = 776351721

is_prime = True
for i in range(2, l):
    if l % i == 0:
        print(i)
        is_prime = False
        break
if is_prime == True:
    print("{0}是质数".format(l))
else:
    print("{0}不是质数".format(l))

r2 = range(1, 4)
res = ''
for i in r2:
    res += str(i)
print(res)
print(','.join(res))
