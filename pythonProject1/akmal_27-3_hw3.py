glasnye = 0
soglasnye = 0

while True:
    word = input('\nВведите слово:').lower()
    for i in word:
        letter = i.lower()
        if letter == "a" or letter == "e" or \
                letter == "i" or letter == "o" or \
                letter == "u" or letter == "y" or \
                letter == "а" or letter == "я" or \
                letter == "у" or letter == "ю" or \
                letter == "о" or letter == "е" or \
                letter == "ё" or letter == "э" or \
                letter == "и" or letter == "ы":
            glasnye += 1

        else:
            soglasnye += 1

    print(f'слово: {word}\n'
          f'Количество букв: {glasnye + soglasnye}\n'
          f'Согласные буквы: {soglasnye}\n'
          f'Гласные буквы: {glasnye }\n')
    glasnye = round(glasnye/ len(word) * 100, 2)
    print("гласные/согласные:", glasnye, "% /", round(100 - glasnye, 2), "%")
    break