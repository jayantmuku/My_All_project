from matplotlib import pyplot as p
data =[12,14,12,11,10,18,17,12,13,14,16,17,18,19,12,12,12]
x=[5,10,15,20,25,30,35,40,45,50,55,60]
p.hist(data,bins=x,ec="red")
p.show()
