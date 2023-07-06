ten = list(range(1, 11))
evens = list(filter(lambda n: n % 2 == 0, ten))
print(evens)
print(list(map(lambda x: x**2, evens)))

def get_by_index(lst=ten):
    while True:
        try:
            index_object = int(input('введите индекс: '))
            print(lst[index_object])
        except ValueError:
            print('вводите только числа!')
        except IndexError:
            print("введите правильный индекс")
        if index_object == 100:
            print('Вы закончили операцию')
            break
get_by_index('python')
