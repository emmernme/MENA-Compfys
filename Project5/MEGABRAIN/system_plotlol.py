import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


file1 = open("Vel 2_0.data", 'r')
file1.readline()

file2 = open("Vel 2_5.data", 'r')
file2.readline()

file3 = open("Vel 2_82.data", 'r')
file3.readline()

file4 = open("Vel 2_83.data", 'r')
file4.readline()


files = [file1, file2, file3, file4]
systems = []
for infile in files:
    info = infile.readline()
    # Get the basic info about the system
    info = info.split(',')
    dim = int(info[0])
    n = int(info[1])
    years = float(info[2])
    dt = float(info[3])
    radius = float(info[4])
    planet_count = int(info[5])

    infile.readline()

    # Get info about and prepare the planets
    planets = []
    for i in range(planet_count):
        planet = infile.readline().split(",")
        planets.append({"name": planet[1].strip(), "position": np.zeros((n-1, dim))})

    infile.readline()

    # Get the positions at each time step
    for i in range(n-1):
        # Get the position for each planet
        for j in range(planet_count):
            pos = infile.readline().split('=')[1].split(',')
            planets[j]["position"][i] = [float(x.strip()) for x in pos]

    systems.append(planets)


plt.style.use("dark_background")
fig = plt.figure()
ax = fig.gca(projection='3d')

plt.gca().patch.set_facecolor('black')
ax.xaxis.set_pane_color((0, 0, 0, 1.0))
ax.yaxis.set_pane_color((0, 0, 0, 1.0))
ax.zaxis.set_pane_color((0, 0, 0, 1.0))
ax.grid(b=False)

for planets in systems:
    for i in range(planet_count):
        pos = planets[i]["position"]
        if (planets[i]["name"] == "Sun"):
            if (dim == 3):
                ax.scatter([0], [0], [0], label=planets[i]["name"], color="#ccff00", linewidth=10)
            else:
                ax.scatter([x[0] for x in pos], [x[1] for x in pos], label=planets[i]["name"], color="#ccff00", linewidth=10)

        else:
            if (dim == 3):
                ax.plot([x[0] for x in pos], [x[1] for x in pos], [x[2] for x in pos], label=planets[i]["name"])
            else:
                ax.plot([x[0] for x in pos], [x[1] for x in pos], label=planets[i]["name"])
    


ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.show()
#plt.savefig('fig1.png')