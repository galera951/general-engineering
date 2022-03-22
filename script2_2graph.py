from matplotlib import pyplot as plt

numbers = [255, 127, 64, 32, 5, 0]
U = [3.259, 1.630, 0.827, 0.501, 0.485, 0.485]


def graph():
    plt.figure()
    plt.scatter(numbers, U)
    plt.plot(numbers, U)
    plt.xlabel("Numbers")
    plt.ylabel("U, V")

    plt.savefig('data.png')