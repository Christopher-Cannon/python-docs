# Print out a list of even powers of 2 from 0 and 30

print([elem for elem in range(20)])

print([elem for elem in range(20) if (elem < 10)])

print([elem for elem in [x**2 for x in range(30)] if (elem % 2 == 0)])
