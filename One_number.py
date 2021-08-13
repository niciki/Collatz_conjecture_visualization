import matplotlib.pyplot as plt

counter = []
n = int(input('Please input a number: '))
plt.title(f'Dependence number of attempts on the {n} of required generations')
while n != 1:
    counter.append(n)
    if n % 2:
        n = 3 * n + 1
    else:
        n /= 2
plt.xlabel("Attempts")
plt.ylabel("Current number")
plt.plot(range(len(counter)), counter)
plt.show()
