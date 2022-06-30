in_str = 'abcd'

lst = [in_str[i] * (len(in_str) - i) for i in range(len(in_str))]
print(lst)