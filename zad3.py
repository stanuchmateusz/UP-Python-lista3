from matplotlib.pyplot import gray


class Fibo:
    def __init__(self, n) -> None:
        self.n = n
        self.a = 0
        self.b = 1

    def __next__(self) -> int:
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self) -> 'Fibo':
        return self


def fibo(n: int, a=0, b=1):
    for _ in range(n):
        a, b = b, a + b
        yield a


def poterzyfib():
    grzyb = [x for x in Fibo(100001)]
    f100k = grzyb[-1]
    f99itd = grzyb[-2]
    # print(len(str(f100k)))  => 20899

    for i in fibo(20, f100k, f99itd):
        yield i


if __name__ == '__main__':
    for i in Fibo(10):
        print(i)

    for i in fibo(10):
        print(i)

    with open('fibo.txt', 'w') as f:
        for i in poterzyfib():
            f.write(str(i) + '\n')
