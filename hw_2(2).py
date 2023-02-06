eng_letters = 'qwertyuiopasdfghjklzxcvbnm'
rus_letters = 'ёйцукенгшщзхъфывапролджэячсмитьбю'


while True:
    word = input('\n Введите слово:')
    if word == 'q':
        print('Программа завершена')
        break
    for i in word:
        if i in eng_letters:
            print(rus_letters[eng_letters.index(i)], end='')
        else:
            print(eng_letters[rus_letters.index(i)], end='')

