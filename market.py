from matplotlib import pyplot as p
import mplcursors as m
Time=["9:00am","10:15am","11:15am","12:15am","1:15pm","2:15pm","3:15pm","4:15pm","6:00pm","6:02pm"]
stock_price=[-8,60,80,55,42,88,70,41,66,55]
p.title("MARKET SUMMARY OF STL LTD",fontsize="20")
p.xlabel("TIME",fontsize="18")
p.ylabel("stock_price",fontsize="18")
p.plot(Time,stock_price,color="red")
p.fill_between(Time,stock_price)
m.cursor(hover=True)
p.ylim(0,90)
p.grid()
p.show()
