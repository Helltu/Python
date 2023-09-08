firstWord = input('Введите первое слово: ')
secondWord = input('Введите второе слово: ')
firstWord = list(firstWord)
firstWord.sort()
secondWord = list(secondWord)
secondWord.sort()
if firstWord == secondWord:
    print('Веденные вами два слова являются анаграммами')
else:
    print('Веденные вами два слова не являются анаграммами')
