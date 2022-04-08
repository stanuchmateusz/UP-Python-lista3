import time
# Napisz klase, której instancja bedzie obiekt nieskończonego iteratora, który bedzie zwracał czas jaki upłynał od jego ostatniego wywołania lub od momentu zdefiniowania przy pierwszym wołaniu.


class Czas:
    def __init__(self) -> None:
        self.start = time.time()

    def __next__(self) -> float:
        return time.time() - self.start

    def __iter__(self) -> 'Czas':
        return self


def czasowy_generator():
    start = time.time()
    while True:
        yield time.time() - start


if __name__ == '__main__':
    c = czasowy_generator()
    # c = Czas()
    for x in c:
        print(x)
