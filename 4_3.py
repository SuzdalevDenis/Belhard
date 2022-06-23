kol = int(input('Введите количество:'))
dict1 = {x: {"name": input(), "email": input()} for x in range(kol)}

print(dict1)