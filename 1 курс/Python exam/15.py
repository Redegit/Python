# На основе строки, представляющей из себя предложение, построить вложенный список, содержащий символы всех слов в
# предложении. Пример: строка 'Eeny, meeny, miney, moe; Catch a tiger by his toe.' будет преобразована
# в: [['E', 'e', 'n', 'y'], ['m', 'e', 'e', 'n', 'y'], ['m', 'i', 'n', 'e', 'y'], ['m', 'o', 'e'],
#     ['C', 'a', 't', 'c', 'h'], ['a'], ['t', 'i', 'g', 'e', 'r'], ['b', 'y'], ['h', 'i', 's'], ['t', 'o', 'e']]

in_str = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'

out_lst = in_str.split()
for i in range(len(out_lst)):
    out_lst[i] = [j for j in out_lst[i] if j.lower() in 'abcdefghijklmnopqrstuvwxyz']
print(out_lst)
