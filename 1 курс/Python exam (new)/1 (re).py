from re import sub


f = open('revizor.txt', 'r', encoding="utf-8")
a = {}

for i in f:
    i = sub(r'[^\w]', ' ', i)
    for j in i.lower().split():
        if j in a:
            a[j] += 1
        else:
            a[j] = 1

a = sorted(a.items(), key=lambda x: x[1], reverse=True)

new_f = open('stat.txt', 'w', encoding="utf-8")
for i in a:
    new_f.write(f'{i[0]} - {i[1]}\n')
