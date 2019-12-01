f = 0
g = 0

r = 1
q = 0

n = 80
a = [[0] * n for i in range(n)]
for i in range(n):
        for j in range(n):
            if i < 1:
                a[i][j] = j
            elif j < 1:
                a[i][j] = i
            else:
                a[i][j] = ' '

for i in range(80):
        f = 0.25*(g-20)**2+1         #function input
        f = round(f)
        g += 1
        i += 1
        if f<80 and g<80 and f>0:
                a[f][g] = '°'

for row in a:
    print(' '.join([str(elem) for elem in row]))


print('')
print("f( g ): ( g | f )")
print('-----------------')
for b in range(n):
        for s in range(n):
                s += 1
                try:
                          print("P(",r,"): ( {0} |".format(b, a[s][b].index('°')), s, ")")
                          r += 1
                except:
                         q += 1
        b += 1
