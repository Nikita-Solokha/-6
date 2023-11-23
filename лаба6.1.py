def count_occurences(s, s0):
s = input(" Введите строку s :")
s0 = input(" Введите строку s0 :")
count = 0
b = count_occo(s, s0)
for i in range(len(s)):
    if s[i] == s0[0]:
        a = 0
        while count < len(s0) and i + a < len(s) and s[i + a] == s0[a]:
            a += 1
        if a == len(s0):
            count = count + 1
print(f"Количество вхождений строки {'s0'} в строке {'s'} :" {b})
