import time
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial as P
import numpy as np
from ex1 import parcours


def plot_function(n, function, expName, expFunc):
    print(f"Ploting {function.__name__} with n = {n} and {expName}")
    x = list()
    y_function = list()
    y_exp = list()
    for i in range(1, n):
        l = np.random.normal(0, i, i).tolist()
        start = time.time()
        function(l)
        end = time.time()
        x.append(i)
        y_function.append(end-start)
        y_exp.append(expFunc(i))

    scaling_factor = y_function[n//2 - 1] / y_exp[n//2 - 1]
    y_exp_scaled = [val * scaling_factor for val in y_exp]

    plt.plot(x, y_function, label=f"{function.__name__} runtime", color="blue")

    plt.plot(x, y_exp_scaled,
             label=f"{expName} curve", color="red", linestyle="--")

    plt.title(
        f"Comparison between {function.__name__} runtime and {expName} curve")
    plt.xlabel("n")
    plt.ylabel(f"Time (or arbitrary units for {expName})")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"computation_times_{function.__name__}_vs_{expName}.pdf")
    plt.close()


plot_function(5000, parcours, "O(n*log(n))", (lambda x: x * np.log(x)))
