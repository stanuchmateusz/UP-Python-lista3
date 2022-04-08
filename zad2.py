def generator(i=1):
    while True:
        yield i
        i += 1


def squaregenerator(n=1):
    for i in generator(n):
        yield i ** 2


def pitagoras():
    # to jest totalnie źle
    for a in squaregenerator(1):
        for b in squaregenerator(a):
            c = a ** 2 + b ** 2
            if c ** 0.5 == int(c ** 0.5):
                yield (a, b, c)


def select(obj, n):
    li = []
    for _ in range(n):
        li.append(next(obj))
    return li


# popsute

def main():
    print(select(pitagoras(), 15))


if __name__ == "__main__":
    main()
