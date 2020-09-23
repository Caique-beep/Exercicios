def absolute(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1


def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(space, 'returning', result)
        return result


def ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


def find(word, letter, index):
    pos = int(index)
    while pos < len(word):
        if word[pos] == letter:
            print(letter)
            return pos
        pos = pos + 1
    return -1


a = find(word='banana', letter='b', index=4)


def count(word: str, letra: str):
    count = 0
    for letter in word:
        if letter == letra:
            count = count + 1
    print(count)


count('casa', 'a')
