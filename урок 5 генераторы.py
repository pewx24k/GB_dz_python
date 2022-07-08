
def gen_new_list(tutors, klasses):
    i = 0
    while i < len(tutors) and i < len(klasses):
        yield tutors[i], klasses[i]
        i += 1
    while i < len(tutors):
        yield tutors[i], None
        i += 1

t = ['Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Ivan', "Petr"]
k = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

for i in gen_new_list(t,k):
    print(i)
print('*'*20)
num_limit=int(input("Введите крайнее число: "))
def gen_range(stop_value, start_value=0, step=1):
    stop_value = stop_value - 1
    current = start_value
    while current < stop_value:
        yield current
        current += step

param = num_limit

obj_gen = gen_range(param, 1, 2)

for i in obj_gen:
    print(i)

items=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
seen = set()
x=[x for x in items if x not in seen and not seen.add(x)]
print(x)


