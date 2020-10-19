import matplotlib.pyplot as plt
import numpy as np

start_num = 100
data = np.loadtxt('b337111NoNum.txt', unpack=True)
x = np.arange(start_num, len(data) + 1)

y = data[start_num-1:len(data)+1]
plt.plot(x, y, label='a(n)')
plt.xlabel('n')
plt.ylabel('y')
plt.title('')
plt.legend()
plt.savefig("A337111.png", dpi=500)
plt.show()

plt.plot(x, np.log(y) / np.log(x),
         label='ln(a(n))/ln(n)')

plt.xlabel('n')
plt.ylabel('y')
plt.title('')
plt.legend()
plt.savefig("A337111LOG.png", dpi=500)
plt.show()

plt.plot(x*np.sqrt(x), y, label='a(n)')

plt.xlabel('n^(3/2)')
plt.ylabel('y')
plt.title('')
plt.legend()
plt.savefig("A337111Gradient.png", dpi=500)
plt.show()
