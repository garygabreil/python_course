# what can be create
# line charts
# bar charts
# pie charts
# histograms

#matplotlib

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,30,40,50]

plt.plot(x,y)
plt.title("Line Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()