time = int(input("Введите число: "))
s = time
m = s // 60
h = m // 60
d = h // 24
if m == 0:
    print(s, "сек")
else:
    if h == 0:
        print(m, "мин", s - m * 60, "сек")
    else:
        if d == 0:
            print(h, "час", m - h * 60, "мин", s - m * 60, "сек")
        else:
            print(d, "дн", h - d * 24, "час", m - h * 60, "мин", s - m * 60, "сек")



cub=list(range(1, 1001, 2))
new_cub=[]
for i in cub:
    new_cub.append(i**3)
print(new_cub)
print(sum(new_cub))

"""for num in range(0,101 ):
    word="процент"
    if (num%10) ==1 and num !=11:
        print(num, word)
    elif 1<(num%10)<=4:
        if 10<num<=14:
            print(num, word +"ов")
        else:
            print(num, word + "a")
    else:
        print(num, word + "ов")"""