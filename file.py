a = 0

def functest():
    global a
    if a < 10:
        print(a)
        a += 1
        functest()

functest()