# (я сделал для txt, из условия не понятно, какой именно тип файлов нужен)

def file(file_name):
    try:
        f = open(file_name, 'r', encoding="utf-8")
    except FileNotFoundError:
        print(f"404. File {file_name} not found")
    else:
        for i in f:
            print(i, end='')


file('stat.txt')
