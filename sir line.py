import matplotlib.pyplot as plt
year=["2001","2005","2010","2015","2020"]
emp=[48,16,20,33,39]
plt.title("year-emp-proverty chart",fontsize="55")
plt.xlabel("year",fontsize="35")
plt.ylabel("Rating",fontsize="35")
plt.plot(year,emp,marker="x",color="green")
plt.show()
