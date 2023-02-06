
all_vowels = "уеыаоэяиюeyuioa"
while True:
    consonants = 0
    vowels = 0
    kol_vo = 0
    word = input("Чтобы выйти из цикла напишите 'выход' или 'exit'\nВведите слово: ").lower()
    if word == 'exit' or word == 'выход':
        print('Программа завершена!')
        break
    for letter in word:
        if letter.isalpha():
            kol_vo += 1
            if letter in all_vowels:
                vowels += 1
            else:
                consonants += 1
    pro = (vowels*100)/len(word)
    pro_gls = round((pro), 2)
print("Кол-во букв:", kol_vo)
print("Кол-во гласных:", vowels)
print("Кол-во согласных:", consonants)
print("Гласные/Согласные:",pro,'%', '/', 100-pro,'%')
