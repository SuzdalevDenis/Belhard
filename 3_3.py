name = "Денис"
age = 19
city = "Минске"
text = "Привет, меня зовут " + name + ", мне " + str(age) + " лет, и я живу в " + city
print(text)

name = "Денис"
age = 19
city = "Минске"
text = "Привет, меня зовут {n}, мне {a} лет, и я живу в {c} ".format(n=name, a=age, c=city)
print(text)

name = "Денис"
age = 19
city = "Минске"
text = f"Привет, меня зовут {name}, мне {age} лет, и я живу в {city}"
print(text)