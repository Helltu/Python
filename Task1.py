F1 = open('F1.txt', 'wt+')
input_line = 'str'
while(input_line):
    input_line = input("Введите строку, которую хотите записать в файл:")
    F1.write(input_line + '\n');
F1.seek(0)
F2 = open('F2.txt', 'wt+')
read_line = F1.readline()
while(read_line):
    read_line = read_line.strip()
    words = read_line.split(" ")
    if(sorted(list(set(words))) != sorted(words)):
        F2.write(read_line+'\n')
    read_line = F1.readline()
F1.seek(0)
F2.seek(0)
F1_text = F1.read().strip()
F2_text = F2.read().strip()
print('Содержимое файла F1.txt:\n' + F1_text + '\n')
print('Содержимое файла F2.txt:\n' + F2_text + '\n')
print('Готово')
F1.close()
F2.close()