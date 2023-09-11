from matplotlib import pyplot as plt
import mplcursors as m
x=[1,2,3,4]
y=[10,20,15,40]
plt.plot(x,y,marker="*")
m.cursor(hover=True)
plt.grid()

plt.show()
