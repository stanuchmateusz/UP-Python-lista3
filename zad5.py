def prime_generator(end):
    for n in range(2, end):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n


def save_to_file(list_of_numbers):
    with open("testfile.txt", "w") as f:
        for i in list_of_numbers:
            f.write(str(i) + '\n')


if __name__ == '__main__':
    tmp = list(prime_generator(10000))
    save_to_file(tmp)
