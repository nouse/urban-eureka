def gen_123():
    yield 1
    yield from gen_2()
    yield from gen_3()


def gen_2():
    yield 2


def gen_3():
    yield 3
