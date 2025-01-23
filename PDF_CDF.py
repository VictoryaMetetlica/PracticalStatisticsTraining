import numpy as np
import matplotlib.pyplot as plt

print('\n   plot the cumulative function graph for the given probability density function')
def function1(x):
    return [el if 0 <= el <= 5 else 0 for el in x]

def function1_INT(x):
    return [
        0.5 * el ** 2 if 0 <= el <= 5 else (0 if el < 0 else 12.5)
        for el in x
    ]

def function3(x):
    return [
        (el if el <= 2.5 else 5 - el) if 0 <= el <= 5 else 0
        for el in x
    ]

def function3_INT(x):
    return [
        ((1/2)*el**2 if el <= 2.5 else 5*el - (1/2)*el**2 ) if 0 <= el <= 5 else (0 if el < 0 else 12.5)
        for el in x
    ]

def function4(x):
    return [
        (2.5 if el <= 2.5 else 5 ) if 0 <= el <= 5 else 0
        for el in x
    ]

def function4_INT(x):
    return [
        (2.5*el if el <= 2.5 else 5 *el) if 0 <= el <= 5 else (0 if el < 0 else 25)
        for el in x
    ]
x = np.arange(-10, 10.01, 0.01)

fig, axs = plt.subplots(3, 2, figsize=(12, 18))

axs[0, 0].plot(x, function1(x))
axs[0, 0].set_title('Function 1 PDF')

axs[0, 1].plot(x, function1_INT(x))
axs[0, 1].set_title('Function 1 CDF')

axs[1, 0].plot(x, function3(x))
axs[1, 0].set_title('Function 2 PDF')

axs[1, 1].plot(x, function3_INT(x))
axs[1, 1].set_title('Function 2 CDF')

axs[2, 0].plot(x, function4(x))
axs[2, 0].set_title('Function 4 PDF')

axs[2, 1].plot(x, function4_INT(x))
axs[2, 1].set_title('Function 4 CDF')

plt.tight_layout()
plt.show()