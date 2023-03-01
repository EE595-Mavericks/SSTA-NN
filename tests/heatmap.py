import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import csv

filename = 'num_100.csv'
x = []
y = []
z = []
x1 = []
y1 = []
z1 = []
error = []

with open(filename, 'r') as f:
    f.readline()
    # reader = csv.reader(f)
    for line in f:
        line.strip('\n')
        result = line.split(',')
        #if float(result[9].strip('\n').strip('%')) >= 0.0001:
        if float(result[8].strip('%')) >= 0.0001:
            x.append(float(result[1]))
            y.append(float(result[2]))
            z.append(float(result[3]))
        else:
            x1.append(float(result[1]))
            y1.append(float(result[2]))
            z1.append(float(result[3]))
        # x.append(float(result[1]))
        # y.append(float(result[2]))
        # z.append(float(result[3]))
        # error.append(float(result[8].strip('%')))

    # x = [float(row[1]) for row in reader]
    # y = [float(row[2]) for row in reader]
    # z = [float(row[3]) for row in reader]
    # error = [float(row[8]) for row in reader]

xx = np.array(x)
yy = np.array(y)
zz = np.array(z)
error_1 = np.array(error)

print(len(z))

# # create some fake data
# x = y = np.arange(-4.0, 4.0, 0.02)
# # here are the x,y and respective z values
# X, Y = np.meshgrid(x, y)
# Z = np.sinc(np.sqrt(X*X+Y*Y))
# # this is the value to use for the color
# V = np.sin(Y)

# create the figure, add a 3d axis, set the viewing angle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(10,75)
ax.set_xlabel('y_mean')
ax.set_ylabel('x_var')
ax.set_zlabel('y_var')

# here we create the surface plot, but pass V through a colormap
# to create a different color for each patch
# ax.plot_surface(xx, yy, zz, facecolors=cm.Oranges(error_1))
ax.scatter(y, x, z, c = 'r')
ax.scatter(y1, x1, z1)

plt.title('step = 100, mean error >= 0.0001%')

plt.show()