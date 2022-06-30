in_str = 'SIX,SEVEN,EIGHT,NINE,TEN'

in_str = in_str.split(',')
out_str = []
for i in range(0, len(in_str), 2):
    out_str.append(in_str[i])
out_str = ','.join(out_str)
print(out_str)
