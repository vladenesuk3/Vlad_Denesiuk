def number_ar(list_of_numbers, target):
    count = 0
    for i in list_of_numbers:
        for j in range(i + 1, len(list_of_numbers)):
            if i + j == target:
                count += 1
    print(count)


x = [1, 3, 6, 2, 2, 0, 4, 5]
number_ar(x, 5)
