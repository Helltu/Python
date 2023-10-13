studies_file = open('studies.txt', 'rt', encoding="utf8")
studies_text = studies_file.read().strip()
print('Содержимое файла studies.txt:\n' + studies_text + '\n')
studies_file.seek(0)
my_dict = dict()
read_line = studies_file.readline()
while read_line:
    my_list = read_line.strip().split()
    value = 0
    for item in my_list:
        try:
            value += int(item.split('(')[0])
        except Exception:
            continue
    try:
        my_dict[my_list[0][0:-1]] = value
    except Exception:
        break
    read_line = studies_file.readline()
print(my_dict)
