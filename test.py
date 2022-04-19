import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('data.txt')
def theor_v(t):
    R = 10 * 100000
    C = 10 * (10 ** (-6))
    tau = R * C

    return 3.3 * (1 - np.exp(-t / tau))

plt.plot(data['time'], theor_v(data['time']))