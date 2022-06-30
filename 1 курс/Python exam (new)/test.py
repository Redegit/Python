a = ['a', 'n']
print(id(a))
a.append('q')
print(id(a[1]))
a[1]='qwe'
print(id(a[1]))