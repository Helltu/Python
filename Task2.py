prices_file = open('prices.txt', 'wt+')
prices_file.writelines(['Микроволновка 2 150\n','Чайник 5 140'])
prices_file.seek(0)
read_line = prices_file.readline()
total_cost = 0;
while read_line:
    my_list = read_line.split(' ')
    line_cost = int(my_list[1]) * int(my_list[2])
    total_cost+=line_cost
    read_line = prices_file.readline()
prices_file.seek(0)
prices_text = prices_file.read()
print('Содержимое файла prices.txt:\n' + prices_text.strip() + '\n')
print('Общая стоимость заказа: ' + str(total_cost))