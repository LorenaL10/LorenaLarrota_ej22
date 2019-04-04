import os
import numpy as np
import matplotlib.pyplot as plt

os.system("g++ metropolis.cpp -o metropolis.x )
os.system("./metropolis.x > datos.dat")

data = np.loadtxt("datos.dat")

plt.figure()
plt.hist(data[:,0], data[:,1])
plt.savefig("datos.png")
