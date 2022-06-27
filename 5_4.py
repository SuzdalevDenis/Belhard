
text = "LONDON"
char = bin(ord("L"))[2:]
char = '0' * (8 - len(char)) + char
char2 = bin(ord("O"))[2:]
char2 = '0' * (8 - len(char2)) + char2
char3 = bin(ord("N"))[2:]
char3 = '0' * (8 - len(char3)) + char3
char4 = bin(ord("D"))[2:]
char4 = '0' * (8 - len(char4)) + char4
char5 = bin(ord("O"))[2:]
char5 = '0' * (8 - len(char5)) + char5
char6 = bin(ord("N"))[2:]
char6 = '0' * (8 - len(char6)) + char6
charx = char + ' ' + char2 + ' ' + char3 + ' ' + char4 + ' ' + char5 + ' ' + char6

key = "SYSTEM"
chart = bin(ord("S"))[2:]
chart = '0' * (8 - len(chart)) + chart
chart2 = bin(ord("Y"))[2:]
chart2 = '0' * (8 - len(chart2)) + chart2
chart3 = bin(ord("S"))[2:]
chart3 = '0' * (8 - len(chart3)) + chart3
chart4 = bin(ord("T"))[2:]
chart4 = '0' * (8 - len(chart4)) + chart4
chart5 = bin(ord("E"))[2:]
chart5 = '0' * (8 - len(chart5)) + chart5
chart6 = bin(ord("M"))[2:]
chart6 = '0' * (8 - len(chart6)) + chart6
chartx = chart + ' ' + chart2 + ' ' + chart3 + ' ' + chart4 + ' ' + chart5 + ' ' + chart6

char_end =
print(charx)
print(chartx)
print(char_end)

mess = input('mess:')
key = input('key:')
if len(mess) != len(key):
    raise ValueError('Blyat')
mess_bin = ''
key_bin = ''
for i in range(len(key):
    char = bin(ord(mess[i]))[2:]
    char = '0' * (8 - len(char)) + char
    mess_bin += char
    char = bin(ord(key[i]))[2:]
    char = '0' * (8 - len(char)) + char
    key_bin += char
    result = ''
for i in range(len(key_bin)):
    if mess_bin[i] != key_bin[i]