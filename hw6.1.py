# def  even_odd (num ):
#     if num % 2 == 0:
#         return True
#     elif num % 2 != 0:
#         return False
#     elif type(num) != int:
#         return None
# print(even_odd(6))




#
#
# def sentence (word):
#     if word[0].isupper() and word[-1] == '.':
#         return word
#     return 'Предложение должно начинаться с большой буквы и заканчиваться точко'
#
#
#
#
# def average(*args):
#     return(int(sum(args) / len(args)))
# print(average(1, 2, 4, 6, 23))
#
#
def b(lst, numer):
    my_lst = []
    for i in lst:
        num2 = i - numer
        my_lst.append(abs(num2))
    index = my_lst.index(min(my_lst))
    print(lst[index])


b([2,3,5,7,3],8)
#
#
# b((3, 6.90, 10, 8), 6.80)





# # 1
# nearest_number = lambda seq, number=0: f'({number}, {sorted(seq, key=lambda x: abs(x - number))})'
# print(nearest_number([5, 20.18, 103, 4], 27))
#
# # 3
# lst = [1, 5, 2.76, 20.22, 6, 4]
#
# new1 = list(map(lambda x: x * 3, lst))
# new2 = tuple(filter(lambda x: type(x) == int, lst))
# print(new1)
# print(new2)


# 2
def function(lst=(list(ten))):
    while True:
        index = input("Введите индекс для вывода объекта из списка:")
        if index.lower() == 'exit' or index.lower() == 'Выход':
            break
        try:
                print(lst[int(index)])
        except:
                print('Неверный индекс или данного индекса не существует')
function()

