day_month = input("Введите день рождения и месяц:")
day = int(day_month[0:2:1])
month = int(day_month[3:])


if (day>=21 and day<=31 and month==3) or(day>=1 and day <=19 and month==4):
    print('Знак зодиака:Овен')
elif (day>=21 and day<=30 and month==4) or (day>=1 and day<=21 and month==5):
    print('Знак зодиака:Телец')
elif (day>=22 and day<=31 and month==5) or (day>=1 and day<=21 and month==6):
    print('Знак зодиака:Близнецы')
elif (day>=22 and day<=30 and month==6) or (day>=1 and day<=22 and month==7):
    print('Знак зодиака:Рак')
elif (day>=23 and day<=31 and month==7) or (day>=1 and day<=21 and month==8):
    print('Знак зодиака:Лев')
elif(day >= 22 and day <= 31 and month == 8) or (day >= 1 and day <= 23 and month == 9):
    print('Знак зодиака:Дева')
elif(day >= 24 and day <= 30 and month == 9) or (day >= 1 and day <= 23 and month == 10):
    print('Знак зодиака:Весы')
elif(day >= 24 and day <= 31 and month == 10) or (day >= 1 and day <= 22 and month == 11):
    print('Знак зодиака:Скорпион')
elif(day >= 23 and day <= 30 and month == 11) or (day >= 1 and day <= 22 and month == 12):
    print('Знак зодиака:Стрелец')
elif(day >= 23 and day <= 31 and month == 12) or (day >= 1 and day <= 20 and month == 0):
    print('Знак зодиака:Козерог')
elif(day >= 21 and day <= 31 and month == 1) or (day >= 1 and day <= 19 and month == 2):
    print('Знак зодиака:Водолей')
elif(day >= 20 and day <= 28 and month == 2) or (day >= 1 and day <= 20 and month == 3):
    print('Знак зодиака:Рыбы')
else:
    print('Неправильный ввод!')
    print('Пример:16/04')






