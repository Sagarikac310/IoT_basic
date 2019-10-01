import matplotlib.pyplot as plt
import csv
import sys

x=[]
y=[]

with open('reading.csv','r') as csvfile:
    plot = csv.reader(csvfile,delimiter=',')
    for row in plot:
        #x.append(int(row[0]))
        x.append((row[1]))
        y.append(float(row[0]))

plt.plot(x,y,label='loaded from file!')
plt.xlabel('dist')
plt.ylabel('time')
plt.title('interesting graph\n check it out')
plt.legend()
plt.show()



