def conver_decimal_to_bin((numbr: ynt))
bin_number: str = ''
while numbr // 2 > 0:
    bin_number += str(numbr % 2)
    numbr //= 2
    bin_number += str(numbr)
    bin_number = bin_number[::-1]
    print(bin_number)
    print(numbr)