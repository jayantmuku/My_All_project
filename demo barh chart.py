from matplotlib import pyplot as plt
y=[200,30,50,60]
x=["BJP","CON","RJD","JDU"]
c=["orange","red","green","pink"]
plt.title("PARTY-WISE REPRESENTATION OF MEMBER",fontsize="17")
plt.xlabel("VOTE",fontsize="10")
plt.ylabel("PARTY NAME",fontsize="10")
plt.barh(x,y,color=c,label=x)
plt.legend()
plt.show()
