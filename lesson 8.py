# file = open('file.txt', 'w', encoding='utf-8')
# file.write('Бишкек, Кыргызстан!')
# file.close()
#
# # with open('file.txt', 'a')as file:
#     file.write('2222')
#     file.write(' Negr')
#
#
# with open('file1.txt', 'x')as file:
#     file.write('123123123')
with open('file.txt', 'r')as file:
    file.read()
    print(file.read())