import matplotlib.pyplot as plt
import matplotlib

xd = [1,2,3,4,5,6,7,8]
ydmax = [10,20,30,40,50,60,70,80]
ydmin = [5,10,15,20,35,30,25,40]
label = ['a','b','c','d','e','f','g','h']

plt.figure()
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 12
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.0
plt.rcParams['ytick.major.width'] = 1.0
plt.rcParams['lines.linewidth'] = 0.8
plt.bar(xd,ydmax)
plt.bar(xd,ydmin,color='white')
plt.xticks(xd, label)
plt.show()
