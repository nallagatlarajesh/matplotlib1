import matplotlib.pyplot as plt
date =["23-12","24-12","25-12","26-12"]
temp= [8.5,10.5,6.8,5.5]
plt.plot(date,temp)#plt.plot())
plt.xlabel("Date")
plt.ylabel("Temp")
plt.title("Date wise temperature")
plt.grid(True)
plt.yticks(temp)
plt.show()
