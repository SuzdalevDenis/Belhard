text = input('Введите текст:')
dict1 = {a: text.count(a) for a in text}
print(dict1)
