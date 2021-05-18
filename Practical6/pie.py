# import mateplotlib
import matplotlib.pyplot as plt
# import numpy
import numpy as np
# pie chart
labels = 'USA','India','Brazil','Russia','UK'
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
# input the size and data
case = dict(zip(labels,sizes))
print(case)
plt.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)
# input some parameter
plt.axis('equal')
plt.title("comparing coronavirus infection rates across countries")
#show the pie chart
plt.show()
