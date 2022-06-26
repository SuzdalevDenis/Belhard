n = int(input('N='))
m = int(input('M='))
k = int(input('K='))
z = [i for i in range(m, (n+1)*m, m)]
if n > k:
    print(z)
else:
    print('Попробуй чуть позже')
