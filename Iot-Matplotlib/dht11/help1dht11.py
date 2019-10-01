import numpy as np
import matplotlib.pyplot as plt
import csv

x=[]
y1=[]
y2=[]
n=68
bar_width=0.6
fig,ax = plt.subplots()
index = np.arange(n)


with open('readingdht11.csv','r') as csvfile:
    plot = csv.reader(csvfile,delimiter=',')
    for row in plot:
        #x.append(int(row[0]))
        x.append((row[2]))
        y1.append((row[0]))
    y2.append((row[1]))

ax.bar(index,y1,bar_width,color='b')
ax.bar(index+bar_width,y2,bar_width,color='g')
plt.xlabel('date')
plt.ylabel('temp,humidity')
plt.title('interesting graph\n check it out')

plt.show()
