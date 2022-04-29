def digits(x):
    summa = 0
    for i in str(x):
        if summa != 0:
            print(f'{summa} + {i} = {summa + int(i)}')
        summa += int(i)
    if summa > 10:
        print('   v   ')
        return digits(summa)


digits(88887)
