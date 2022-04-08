def gen_time(start, end, step):
    starten = truple_to_time(start)
    enden = truple_to_time(end)
    stepen = truple_to_time(step)
    while starten < enden:
        yield time_to_truple(starten)
        starten += stepen


def truple_to_time(t):
    return t[0] * 3600 + t[1] * 60 + t[2]


def time_to_truple(t):
    return t // 3600, (t % 3600) // 60, t % 60


if __name__ == '__main__':
    for i in gen_time((8, 10, 0), (10, 50, 0), (0, 15, 12)):
        print(i)
