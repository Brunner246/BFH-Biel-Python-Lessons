def add_one(value: int) -> int:
    return value + 1


add_one_lambda = lambda value: value + 1  # \x -> x + 1


# add_one_lambda(1) -> 2


def add(x: int, y: int) -> int:
    return x + y


add_lambda = lambda x, y: x + y  # \x y -> x + y
# add_lambda(1, 2) -> 3


if __name__ == '__main__':
    print(add_one(1))
    print(add_one_lambda(1))
    print(add(1, 2))
    print(add_lambda(1, 2))
