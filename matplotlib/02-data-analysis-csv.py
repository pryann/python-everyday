import numpy as np
from matplotlib import pyplot as plt

# bar - overlaping by default
# np.arange
# replace ages_x to x_indexes
# width
# xticks

plt.style.use('seaborn-v0_8-bright')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# plt.plot(ages_x, dev_y, 'k--', label="Python devs")
plt.bar(x_indexes - width, dev_y, width=width,
        color="#000000",  label="All devs")

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Add a second line
plt.bar(x_indexes, py_dev_y, width=width,
        color='#0000FF',  label="Python devs")


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes + width, js_dev_y, width=width,
        color='#FFFF00', label="JS devs")


# Add labels
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.title("Median Salary (USD) by age")

plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.grid(True)

plt.tight_layout()

plt.savefig('plot.svg')

plt.show()
