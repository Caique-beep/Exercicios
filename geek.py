def weird(n):
    if 1 <= n and n >=100:
        if n % 2 == 0:
            return print("weird")
        elif n in range(2,6):
            return print("not weird")
        elif n in range(6,20):
            return print("Weird")
        elif n >= 20:
            return print("Not weird")
    else:
        return print("O numero tem que ser entre 1 e 100")




weird(3)
weird(24)