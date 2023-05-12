# Реализовать однонаправленный связанный список (реализовать класс для элементов списка).
# Преобразовать строку 'Eeny, meeny, miney, moe; Catch a tiger by his toe.' в связный список символов строки
# и удалить из него все элементы содержащие гласные буквы

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.reference = None
#
#     def append(self, data):
#         end_node = Node(data)

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append(self, val):
        end = Node(val)
        n = self
        while n.next:
            n = n.next
        n.next = end


in_str = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'

a = Node(1)
print(a.data)
a.append(3)
a = a.next
print(a.data)
