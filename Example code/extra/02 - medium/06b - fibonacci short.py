a, b, seq = 0, 1, [0, 1]
for x in range(50): a, b, seq[len(seq):] = b, a + b, [a + b]
print(seq)
