from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import math

import csv

heat_lats = []
heat_lons = []
elevation = []
signal = []

with open('planelog.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        elevation.append(float(row[3]))
        heat_lats.append(float(row[4]))
        heat_lons.append(float(row[5]))
        signal.append(float(row[6]))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(heat_lons, heat_lats, elevation)

plt.xlim(7, 9)
plt.ylim(46, 48)

plt.show()