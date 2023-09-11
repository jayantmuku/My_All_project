from matplotlib import pyplot as plt
x=["BJP","CON","RJD","JDU"]
y=[200,30,50,60]
c=["orange","red","green","pink"]
plt.title("PARTY-WISE REPRESENTATION OF MEMBER",fontsize="17")
plt.ylabel("VOTE",fontsize="10")
plt.xlabel("PARTY NAME",fontsize="10")
plt.bar(x,y,color=c,label=x)
plt.legend()
plt.show()
