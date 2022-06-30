inp_str = input().split()

counter = 0
for i in inp_str:
    if i[0] == i[-1]:
        counter += 1

print(counter)
