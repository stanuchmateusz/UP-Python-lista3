from typing import Iterable


def to_single_array(el):

    if isinstance(el, Iterable) and not isinstance(el, str):
        for i in el:
            yield from to_single_array(i)
    else:
        yield el


if __name__ == '__main__':

    l = []
    for x in to_single_array([1, "aaa", (2, 3, 4), [5, 6, 7], [56, "kot"]]):
        l.append(x)
    print(l)
