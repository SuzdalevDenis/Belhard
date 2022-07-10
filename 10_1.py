list_text = [0, 1, 2, 3, 4, 3, 2, 1, 0]
for i in range(len(list_text)//2):
    if list_text[i] != list_text[-i-1]:
        print('не верно')
        break
else:
    print('верно')