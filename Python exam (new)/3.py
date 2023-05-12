def type_change(ar):
    if type(ar) != list:
        tmp = ar
        ar = []
        ar.append(tmp)
    a = []
    for i in range(len(ar)):
        if ar[i] == 'True':
            a.append(True)
        elif ar[i] == 'False':
            a.append(False)
        elif ar[i].lstrip('-').isdigit():
            a.append(int(ar[i]))
        elif '.' in ar[i] and ar[i].lstrip('-').replace('.', '').isdigit():
            a.append(float(ar[i]))
        elif '[' in ar[i]:
            a.append(type_change(ar[i].lstrip('[').rstrip(']').split(',')))
        elif '{' in ar[i]:
            tmp = ar[i].lstrip('{').rstrip('}').split(':')
            a.append({type_change(tmp[i]): type_change(tmp[j]) for i, j in zip(range(0, len(tmp) - 1, 2), range(1, len(tmp), 2))})
        elif '(' in ar[i]:
            a.append(tuple(type_change(ar[i].lstrip('(').rstrip(')').split(','))))
        else:
            a.append(str(ar[i].strip("""'""")))
    if len(a) == 1:
        return a[0]
    else:
        return a


f = open('myfile.txt', 'r')
a = f.readline()
a = a.lstrip('[').rstrip(']').split(', ')

a = type_change(a)

a_dig = []
a_other = []
for i in a:
    a_dig.append(i) if type(i) == int or type(i) == float else a_other.append(i)

a_dig = sorted(a_dig)
a_dig.extend(a_other)
print(a_dig)

f.close()
f = open('myfile_new.txt', 'w')
f.write(str(a_dig))
