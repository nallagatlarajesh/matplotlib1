#line chart using matlotlb.pyplot as plt
import matplotlib.pyplot as plt
#lisst storing date in string format
date =["25/12","26/12","27/12"]
temp=[8.5,10.5,6.8]

#create a figure plotting temp versus date
plt.plot(date,temp)

#show thw figure
plt.show()
