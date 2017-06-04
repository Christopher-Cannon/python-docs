def fibonacci(limit):
    a, b, seq = 0, 1, [0, 1]
    for x in range(limit): a, b, seq[len(seq):] = b, a + b, [a + b]
    return seq

print(fibonacci(int(input("How many numbers to generate? -> "))))
