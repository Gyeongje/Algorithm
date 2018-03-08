def base64_encode(str):
    b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    p = 0
    dest = []
    s = []
    en = []
    en_str = ''

    for i in str:
        s += en_binary_number(ord(i))

    arr = []
    for i in range(len(s)):
        arr.append(s[i])
        if (i + 1) % 6 == 0 and i != 0:
            dest.append(arr)
            arr = []

    if len(arr) % 6 != 0:
        p = (6 - len(arr)) / 2  # padding count
        for i in range(len(arr), 6):
            arr.append(0)
        dest.append(arr)

    for i in range(len(dest)):
        en.append(en_demical_number(dest[i]))

    for i in range(len(en)):
        en_str += b64_table[en[i]]

    en_str += (b64_table[64] * p)

    return en_str


def base64_decode(str):
    b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    dest = []
    s = []
    de = []
    de_str = ''

    for i in str:
        if i != '=':
            s += de_binary_number(b64_table.index(i))

    arr = []
    for i in range(len(s)):
        arr.append(s[i])
        if (i + 1) % 8 == 0 and i != 0:
            dest.append(arr)
            arr = []

    for i in range(len(dest)):
        de.append(de_demical_number(dest[i]))

    for i in range(len(de)):
        de_str += chr(de[i])

    return de_str


def en_binary_number(str):
    bin = [0 for i in range(8)]
    for i in range(7, -1, -1):
        bin[i] = str & 1
        str >>= 1
    return bin


def en_demical_number(str):
    num = str[0]
    for i in range(1, 6):
        num = num * 2 + str[i]
    return num


def de_binary_number(str):
    bin = [0 for i in range(6)]
    for i in range(5, -1, -1):
        bin[i] = str & 1
        str >>= 1
    return bin


def de_demical_number(str):
    num = str[0]
    for i in range(1, 8):
        num = num * 2 + str[i]
    return num


if __name__ == '__main__':
    print '1. base64 encoding'
    print '2. base64 decoding'
    n = input("> ")
    str = raw_input("input string : ")
    if n == 1:
        en = base64_encode(str)
        print 'encode : ' + en
    elif n == 2:
        de = base64_decode(str)
        print 'decode : ' + de
    else:
        exit(1)
        
#made by Gyeongje
