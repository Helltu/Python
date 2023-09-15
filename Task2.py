text = input('Введите текст, из которого нужно удалить все слова, оканчивающиеся на букву "а": ')
wordArray = text.split(' ')
resArray = []
for item in wordArray:
    if item[-1] != 'а':
        resArray.append(item)
if len(resArray) == 0:
    print('Нет слов, не заканчивающихся на букву "а"')
else:
    print(' '.join(resArray))

