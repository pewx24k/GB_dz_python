import os.path

base_dir = 'my_project'
inside_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']

for dir_name in inside_dirs:
    os.makedirs(os.path.join(base_dir, dir_name), exist_ok=True)

"""import os.path
import shutil

base_dir = 'my_project'
mother_templates = os.path.join(base_dir, 'templates')

if not os.path.exists(mother_templates):
    os.mkdir(mother_templates)

for root, dirs, files in os.walk(base_dir):
    if len(dirs) > 0:
        if dirs[0] == 'templates':
            shutil.copytree(os.path.join(root, dirs[0]), mother_templates, dirs_exist_ok=True)

import os
import os.path

limits = [100, 1000, 10000, 100000]
folder = 'some_data'
res_dict = dict.fromkeys(limits, 0)
size_list = []
for root, dirs, files in os.walk(folder):
    for file in files:
        size_list += [os.stat(os.path.join(root, file)).st_size]

for size in size_list:
    for limit in limits:
        if size <= limit:
            res_dict[limit] += 1
            break
print(len(size_list), 'файлов')
print('\t{')
for k, v in res_dict.items():
    print('\t', f'{k}: {v}')
print('\t}')"""