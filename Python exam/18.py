# Реализовать функцию par_val, которая принимает на вход заранее неизвестное количество именованных параметров
# (значения параметров - строки) и возвращает список имен параметров, которым соответствуют строки, содержащие
# более двух слов. Пример: par_val(pp='abba war', fan='oneword', zr='a x') -> [pp, zr]
# !В условии ошибка: просят более двух слов, но в примере работает и с двумя ('abba war')
# Плюс почему-то в примере нет кавычек ([pp, zr]), не понятно, это баг или фича

def par_val(**p):
    lst = []
    for key, val in p.items():
        if len(val.split()) >= 2:
            lst.append(key)
    return lst


print(par_val(pp='abba war', fan='oneword', zr='a x'))
