text = input('Введите текст:')
dict1 = {i: text.count(i) for i in text}
print(dict1)
