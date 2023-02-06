countries = {
    'kg': {'red', 'yellow'},
    'rus': {'red', 'blue', 'white'},
    'usa': {'white', 'red', 'blue'},
    'ua': {'yellow', 'blue'}
}

while True:
    s = input('Введите цвета флагов: ').split()
    if len(s) == 1 and s[0].lower() == 'exit':
        print('ПРОГРАММА ОСТАНОВЛЕНА')
        break
    p = 0
    for i, j in countries.items():
        sum = 0
        for k in s:
            if k in j:
                sum += 1
        if sum == len(s):
            print(i)
            p += 1
    if p == 0:
        print('Нет флага у которого есть эти цвета')