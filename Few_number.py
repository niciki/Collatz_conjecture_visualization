import matplotlib.pyplot as plt

counter = []
n1 = int(input('Please input a lower bound of interval: '))
n2 = int(input('Please input an upper bound of interval: '))
plt.title(f'Dependence number of attempts for each number in interval [{n1}, {n2}]')
for i in range(n1, n2 + 1):
    cnt = 0
    while i != 1:
        cnt += 1
        if i % 2:
            i = 3 * i + 1
        else:
            i /= 2
    counter.append(cnt)
plt.ylabel("Attempts for number")
plt.xlabel(f'Number\n Orange - number of attempts sorted\n Green - number of attempts for each number\n Maximal number of attempts in this interval for a number {max(counter)} is {counter.index(max(counter))}')
plt.plot(range(len(counter)), counter)
plt.plot(range(len(counter)), sorted(counter))
plt.show()
