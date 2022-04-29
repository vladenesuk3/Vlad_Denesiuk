letter_repeat = 'ascafc'


def first_not_repeat_letter(let_rep):
    list_repeat = []
    counts = {}
    for x in let_rep:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
            list_repeat.append(x)
    for x in list_repeat:
        if counts[x] == 1:
            return f'{x} - first letter that does not repeat'
    return None


print(first_not_repeat_letter(letter_repeat))
