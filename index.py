import matplotlib.pyplot as plt

dataset = [[1.2, 1.1], [2.4, 3.5], [4.1, 3.2], [3.4, 2.8], [5, 5.4]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]
plt.axis([0, 6, 0, 6])
plt.plot(x, y, 'bs')
plt.grid()
plt.show()
plt.savefig('scatter.png')

def mean(values):
    return sum(values) / float(len(values))

def variance(values, mean):
    return sum([(x-mean)**2 for x in values])
