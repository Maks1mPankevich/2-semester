#Labrab-01
import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(-10, 15, 100)
y = 10*x**3 - 500
fig, ax = plt.subplots()
ax.plot(x,y, color = 'blue')
ax.vlines(0, y.min(), y.max(), color = 'red')
ax.hlines(0, x.min(), x.max(), color = 'red')
plt.show()