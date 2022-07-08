"""print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

"""

"""new=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i=0
while i<len(new):
    if new[i].isdigit():
        new[i]=new[i].zfill(2)
    elif new[i].startswith("+"):
        new[i]=new[i].zfill(3)
    i+=1
n=1
while n<len(new):
    if new[n].isdigit() or new[n].startswith("+") and new[n][1:].isdigit():
        new.insert(n, '"')
        new.insert(n+2, '"')
        n +=1
    n+=1
print(new)
print(" ".join(new))"""

a = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
     'токарь высшего разряда нИКОЛАй', 'директор аэлита']
b = {}
for i in a:
    b = i.split()[-1].capitalize()
    print(f'Привет {b}')

my_list = [54.6, 123.3, 55, 87.7, 91, 83, 43.5, 42.3]
for i in my_list:
    rub = int(i)
    kop = str(round((i - rub) * 100)).zfill(2)
    print(f'{rub} руб. {kop}коп.')
my_list.sort()
print(my_list)

