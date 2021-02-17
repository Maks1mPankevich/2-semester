#Labrab-01
import matplotlib.pyplot as plt 
import numpy as np
def func(x,a,b,c,t):
    return (a*x**2+b*x+c) / (x+t)
styles = plt.style.available
plt.style.use(styles[8]) 
a = 10; b = 270; c = 90; t = -8
legend = 'y = {}*x**2+{}*x+{}'.format(a,b,c)
left = -100; right = 100; step =0.5
data_x=[]; data_y=[]
pos_x=0
while pos_x <= right:
    try:
        pos_y = func(pos_x, a, b, c, t)
        data_x.append([pos_x])
        data_y.append([pos_y])
    except:
        pass
    pos_x += step
# data_x = np.arange(left, right, step)
# data_y = [func(x,a,b,c) for x in data_x]
plt.plot(data_x, data_y)
plt.title("График функции")
plt.xlabel("Ось Х")
plt.ylabel("Ось Y")
plt.legend([legend])
plt.grid(True)
plt.axhline(color='orange')
plt.axvline(color='orange')
plt.show()
