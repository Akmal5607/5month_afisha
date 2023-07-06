# w - режим записи, перезаписи
# a - режим записи, дозаписи
# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан')
# file.close()

# with open('file.txt', 'w', encoding='UTF=8') as file:
#     file.write('новая строка')
# with open('file2.txt', 'x', encoding='UTF=8') as file:
#     file.write('новая строка')


with open('file.txt', 'r', encoding='UTF=8') as file:
    file.readline()
    print(file.read())
    