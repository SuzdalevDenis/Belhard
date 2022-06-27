
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