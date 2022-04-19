import matplotlib.pyplot as plt

voltage = [(1, 3), (2, 5)]

with open('data.txt', 'w') as outfile:
    plt.scatter(voltage)
    plt.xlabel('t, с')
    plt.ylabel('U, В')
    plt.title('Зависимость напряжения на обкладках конденсатора U от времени t')
    plt.show()
    
    str_voltage = [str(u) for u in voltage]
    out = '\n'.join(str_voltage)
    outfile.write(out)

