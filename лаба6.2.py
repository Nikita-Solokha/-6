a = input(" Введите слово: ")
b = ''
for i in range(len(a)):
    b += a [(i + 1) % len (a)]
print(" Готовое слово: ", b)