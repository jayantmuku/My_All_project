from matplotlib import pyplot as plt
gas=[73,21,2,1]
name=["NITROGEN","OYXGEN","OTHERGAS","CO2"]
e=[0,0.1,0.1,0]
plt.pie(gas,labels=name,autopct="%0.1f%%",explode=e)
plt.show()
