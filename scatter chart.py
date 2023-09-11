from matplotlib import pyplot as plt
import mplcursors as m
x=["MOHAN","RAHUL","AAKASH","RAJU"]
y=[80,70,77,81]
plt.scatter(x,y)

x=["MOHAN","RAHUL","AAKASH","RAJU"]
y=[88,97,66,33]
plt.scatter(x,y)
plt.grid()
x=["MOHAN","RAHUL","AAKASH","RAJU"]
y=[8,7,7,8]
plt.scatter(x,y)
m.cursor(hover=True)
plt.ylim(1,10)
plt.show()
