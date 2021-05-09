# Old way
print(2**3)

# Another Way by function


def raise_to_power(base_num, pow):
    result = 1
    for i in range(pow):
        result = result * base_num
    return result


print(raise_to_power(2, 3))
