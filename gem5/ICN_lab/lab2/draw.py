import matplotlib.pyplot as plt
import numpy as np
import math

injection_rate = np.arange(0.02, 1, 0.02).tolist()

# uniform_random ---------------------------------------------------
mesh_uniform_random = []
flattenedbutterfly_uniform_random = []

# mesh
f_mesh = open("./result/mesh_uniform_random.txt")
line = f_mesh.readline() # drop "average packet latency"
line = f_mesh.readline()
while(line):               
    print(line, end = '')
    mesh_uniform_random.append(math.log(float(line)))
    line = f_mesh.readline()  
f_mesh.close()  

# flattenedbutterfly
f_flattenedbutterfly = open("./result/flattenedbutterfly_uniform_random.txt")
line = f_flattenedbutterfly.readline() # drop "average packet latency"
line = f_flattenedbutterfly.readline()
while(line):               
    print(line, end = '')
    flattenedbutterfly_uniform_random.append(math.log(float(line)))
    line = f_flattenedbutterfly.readline()  
f_flattenedbutterfly.close()  

plt.plot(injection_rate, mesh_uniform_random, label='Mesh_XY', marker='o')
plt.plot(injection_rate, flattenedbutterfly_uniform_random, label='FlattenedButterfly', marker='o')
plt.title('average packet latency VS injection rate (uniform_random)')
plt.xlabel('injection rate')
plt.ylabel('log(average packet latency)')
plt.legend()
plt.savefig("uniform_random.png")
plt.clf()


# tornado ---------------------------------------------------
mesh_tornado = []
flattenedbutterfly_tornado = []

# mesh
f_mesh = open("./result/mesh_tornado.txt")
line = f_mesh.readline() # drop "average packet latency"
line = f_mesh.readline()
while(line):               
    print(line, end = '')
    mesh_tornado.append(math.log(float(line)))
    line = f_mesh.readline()  
f_mesh.close()  

# flattenedbutterfly
f_flattenedbutterfly = open("./result/flattenedbutterfly_tornado.txt")
line = f_flattenedbutterfly.readline() # drop "average packet latency"
line = f_flattenedbutterfly.readline()
while(line):               
    print(line, end = '')
    flattenedbutterfly_tornado.append(math.log(float(line)))
    line = f_flattenedbutterfly.readline()  
f_flattenedbutterfly.close()  

plt.plot(injection_rate, mesh_tornado, label='Mesh_XY', marker='o')
plt.plot(injection_rate, flattenedbutterfly_tornado, label='FlattenedButterfly', marker='o')
plt.title('average packet latency VS injection rate (tornado)')
plt.xlabel('injection rate')
plt.ylabel('log(average packet latency)')
plt.legend()
plt.savefig("tornado.png")
plt.clf()

# neighbor ---------------------------------------------------
mesh_neighbor = []
flattenedbutterfly_neighbor = []

# mesh
f_mesh = open("./result/mesh_neighbor.txt")
line = f_mesh.readline() # drop "average packet latency"
line = f_mesh.readline()
while(line):               
    print(line, end = '')
    mesh_neighbor.append(math.log(float(line)))
    line = f_mesh.readline()  
f_mesh.close()  

# flattenedbutterfly
f_flattenedbutterfly = open("./result/flattenedbutterfly_neighbor.txt")
line = f_flattenedbutterfly.readline() # drop "average packet latency"
line = f_flattenedbutterfly.readline()
while(line):               
    print(line, end = '')
    flattenedbutterfly_neighbor.append(math.log(float(line)))
    line = f_flattenedbutterfly.readline()  
f_flattenedbutterfly.close()  

plt.plot(injection_rate, mesh_neighbor, label='Mesh_XY', marker='o')
plt.plot(injection_rate, flattenedbutterfly_neighbor, label='FlattenedButterfly', marker='o')
plt.title('average packet latency VS injection rate (neighbor)')
plt.xlabel('injection rate')
plt.ylabel('log(average packet latency)')
plt.legend()
plt.savefig("neighbor.png")
plt.clf()

