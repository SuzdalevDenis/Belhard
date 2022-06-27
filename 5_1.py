n = int(input('N='))
m = int(input('M='))
k = int(input('K='))
z = [i for i in range(m, (n+1)*m, m)]
if n > k:
    print(z)
else:
    print('Попробуй чуть позже')

n = int(input('n='))
m = int(input('m='))
k = int(input('k='))
i = k
count = 0
while count < n:
    if not i % m:
        count +=1
        print(i)
    i +=1