ans="yes"
while(ans=="yes"):
    from matplotlib import pyplot as plt
    p=[]
    s=[]
    for i in range (3):
        arty=input("ENTER ANY PARTY NAME")
        p.append(party)
        seat=int(input("ENTER NO.OF SEATS"))
        s.append(seat)
    plt.plot(p,s)
    plt.show()
print("DO YOU WANT TO CONTINEW(yes/no")
             
