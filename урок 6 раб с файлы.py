from  collections import Counter
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    my_dict=Counter()
    for i in f:
        my_dict[i.split()[0]] += 1
    ip, count = my_dict.most_common(1)[0][0], my_dict.most_common(1)[0][1]
    print(f'Spammer {ip} - {count}times')
    print(my_dict.most_common(5))

from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        all_list = zip_longest((' '.join(us.split(",")) for us in users), hobby, fillvalue=None)
        my_dict = {str(el[0]).strip(): str(el[1]).strip() if [0] else exit(1) for el in all_list}

        with open('dict_n_json','w', encoding='utf-8') as f:
            dump(my_dict, f, ensure_ascii=False, indent=4)
            print(my_dict)

from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as donut:
    if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:
        if len(argv) == 3:
            start, finish = map(int, argv[1:])
            print(*(v for i, v in enumerate(donut) if start - 1 <= i < finish), sep='')
        else:
            print(*(v for i, v in enumerate(donut) if i >= int(argv[1]) -1), sep='')
    else:
        print(donut.read())