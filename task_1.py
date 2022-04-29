def task_1(list_x: list):
    list_x = [i for i in list_x if type(i) is not str]
    return list_x


a = [1, 2, 'a', 'b']
print((task_1(a)))
