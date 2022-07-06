import random
"""try:
    num = {"one":"один", "two":"два", "three":"три", "four":"четыре", "five":"пять",
            "six":"шесть", "seven":"семь", "eight":"восемь", "nine":"девять", "ten":"десять"}
    a=str(input("Какое число перевести?: "))
    print(f' {num[a]}')
except KeyError:
    print('Нужно число от одного до десяти')
"""

"""words=("Иван", "Мария", "Петр", "Илья")
r={}
for i in words:
    key=i[:1]
    r[key]=i
print(r)"""



nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

a = int(input("Сколько раз прошутить? "))
b=0
#для того чтобы была возможность генерировать шутки больше одного раза
while b != a:
    for n, adv, adj in zip(nouns, adverbs, adjectives):
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
    print(f'{n} {adv} {adj}')
    b+=1
