import matplotlib.pyplot as plt 

steps = [6543, 7000, 8900, 10789, 3467, 11045, 5095]
labels = [1,2,3,4,5,6,7]
plt.bar(labels, steps, align='center')

plt.ylabel('Steps')
plt.xlabel('Day')
plt.title('Number of steps walked')

plt.grid()
plt.show()
