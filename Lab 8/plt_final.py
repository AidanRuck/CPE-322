import matplotlib.pyplot as plt
from pandas import *
from scipy import stats

data = read_csv('cpudata.csv')
x = data['CPU Usage (%)']
y = data['Memory Available (GB)']

# Time series
plt.plot(y, 'r', lw=2, label='Memory Available (in GB)')
plt.plot(x, 'b', lw=2, label='CPU Usage (%)')
plt.xticks([209,452,703,957],['21:00','21:30','22:00','22:30'])
plt.xlabel('Time')
plt.legend(loc='lower center')
plt.title('DREBUFS 2025-05-04')

# Histogram of CPU usage
plt.figure()
num_bins = 35
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue', alpha=0.5)
plt.xlabel('CPU Usage (%)')
plt.ylabel('Probability')
plt.title('DREBUFS 2025-05-04')

# Histogram of temperature
plt.figure()
num_bins = 30
n, bins, patches = plt.hist(y, num_bins, density=1, facecolor='red', alpha=0.5)
plt.xlabel('Memory Available (GB)')
plt.ylabel('Probability')
plt.title('DREBUFS 2025-05-04')

# Horizontal box plot of CPU usage
plt.figure()
plt.boxplot(x, 0, '+', 0)
plt.xlabel('CPU Usage (%)')
plt.title('DREBUFS 2025-05-04')

# Vertical box plot of temperature
plt.figure()
plt.boxplot(y, 0, '+')
plt.ylabel('Memory Available (GB)')
plt.title('DREBUFS 2025-05-04')

# Scatter diagram with a linear regression line
plt.figure()
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.xlabel('CPU Usage (%)')
plt.ylabel('Memory Available (GB)')
plt.plot(x, y, 'bo')
l = [slope * i + intercept for i in x]
plt.plot(x, l, 'r', lw=2)
plt.title('DREBUFS 2025-05-04')

plt.show()
