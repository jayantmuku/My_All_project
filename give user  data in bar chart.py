from matplotlib import pyplot as plt
p=[]
s=[]
for i in range (3):
    party=input("ENTER ANY PARTY NAME")
    p.append(party)
    seat=int(input("ENTER NO.OF SEATS"))
    s.append(seat)
plt.bar(p,s)
plt.show()
             
