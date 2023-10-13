import json

firms_file = open('firms.txt', 'rt', encoding="utf8")
firms_text = firms_file.read().strip()
print('Содержимое файла firms.txt:\n' + firms_text + '\n')
firms_file.seek(0)
firms = dict()
average = dict()
read_line = firms_file.readline()
count = 1;
totalIncome = 0;
while(read_line):
    my_list = list(map(lambda x: x.strip() , read_line.split()))
    try:
        income = int(my_list[2]) - int(my_list[3])
        totalIncome += income
        firms[my_list[0]] = income
        read_line = firms_file.readline()
        count+=1
    except IndexError:
        break
average["average_profit"] = totalIncome/(count-1)
print(firms, average)
firms_file.close()

with open("firms.json", 'w') as firms_json:
    res_list = list()
    res_list.append(firms)
    res_list.append(average)
    json.dump(res_list, firms_json)
    