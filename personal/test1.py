def count():
    c = 1
    while True:
        for i in range(c):
            print(", ".join([str(i + 1) for i in range(c)]))
        c += 1

count()