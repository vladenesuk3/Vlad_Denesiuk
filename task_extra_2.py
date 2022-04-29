def uns_to_ipv4(num):
    first = num//256**3
    second = (num - first*256**3) // 256**2
    third = (num - first*256**3 - second*256**2) // 256
    fourth = (num - first*256**3 - second*256**2 - third * 256)
    return f'{first}.{second}.{third}.{fourth}'


print(uns_to_ipv4(2149583361))
print(uns_to_ipv4(32))
print(uns_to_ipv4(0))
