import matplotlib.pyplot as plt
import numpy as np
import json
from io import StringIO
plt.ioff()
def plot_triang(list_vertices=[0,1,2,3,4,5],index=0,n=6, radius=1):
    angles_small = np.linspace(0, 2 * np.pi, 100, endpoint=False)
    x_coords_small = radius * np.cos(angles_small) * 0.1
    y_coords_small = radius * np.sin(angles_small) * 0.1
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x_coords = radius * np.cos(angles)
    y_coords = radius * np.sin(angles)

    x_coords_loops = 1.1 * radius * np.cos(angles)
    y_coords_loops = 1.1 * radius * np.sin(angles)
    
    contains_no_hi=True
    # for k in range(n+(n*(n-1))//2,2*n+(n*(n-1))//2):
    #     if k in list_vertices:
    #         contains_no_hi = False
    #         break
    if contains_no_hi:
        plt.figure(figsize=(6, 6))  # Optional: Set the figure size
        plt.axis('off')
        for v in list_vertices:
            if v<n:
                plt.plot(x_coords_loops[v]+x_coords_small, y_coords_loops[v]+y_coords_small, marker='', linestyle='-', color='b')
            elif v<n+(n*(n-1)//2):
                r = v%n
                q = v//n
                plt.plot([x_coords[r],x_coords[(q+r)%n]], [y_coords[r],y_coords[(q+r)%n]], marker='', linestyle='-', color='b')

            else:
                u = v-n - n*(n-1)//2
                plt.plot(x_coords[u]+x_coords_small, y_coords[u]+y_coords_small, marker='', linestyle='-', color='r')
        for k in range(n):
            plt.plot(x_coords[k], y_coords[k], marker='o', linestyle='-', color='black')
        plt.axis('equal')  # Equal aspect ratio for x and y axes
        plt.savefig("./n"+str(n)+"_type2_fig/fig_"+str(index)+".pdf",dpi=50)
        plt.close()

def plot_triang_type1(list_vertices=[0,1,2,3,4,5],index=0,n=6, radius=1):
    angles_small = np.linspace(0, 2 * np.pi, 100, endpoint=False)
    x_coords_small = radius * np.cos(angles_small) * 0.1
    y_coords_small = radius * np.sin(angles_small) * 0.1
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x_coords = radius * np.cos(angles)
    y_coords = radius * np.sin(angles)

    x_coords_loops = 1.1 * radius * np.cos(angles)
    y_coords_loops = 1.1 * radius * np.sin(angles)
    
    contains_no_hi=True
    # for k in range(n+(n*(n-1))//2,2*n+(n*(n-1))//2):
    #     if k in list_vertices:
    #         contains_no_hi = False
    #         break
    if contains_no_hi:
        plt.figure(figsize=(6, 6))  # Optional: Set the figure size
        plt.axis('off')
        for v in list_vertices:
            if v<n:
                plt.plot(x_coords_loops[v]+x_coords_small, y_coords_loops[v]+y_coords_small, marker='', linestyle='-', color='b')
            elif v<n+(n*(n-1)//2):
                r = v%n
                q = v//n
                plt.plot([x_coords[r],x_coords[(q+r)%n]], [y_coords[r],y_coords[(q+r)%n]], marker='', linestyle='-', color='b')

            else:
                plt.plot(0+x_coords_small, 0+y_coords_small, marker='', linestyle='-', color='g')
        for k in range(n):
            plt.plot(x_coords[k], y_coords[k], marker='o', linestyle='-', color='black')
        plt.axis('equal')  # Equal aspect ratio for x and y axes
        plt.savefig("./n"+str(n)+"_type1_fig/fig_"+str(index)+".pdf",dpi=50)
        plt.close()

def print_type2(n):
    PATH_file = 'triang_n'+str(n)+'type_2.out'
    with open(PATH_file) as f:
        lines_str = [line.strip() for line in f]
    lines = []
    for line in lines_str:
        lines.append([int(v) for v in line.strip('} {').split(' ')])

    for k in range(len(lines)):
        triang = lines[k]
        plot_triang(triang,k,n)

def print_type1(n):
    PATH_file = 'triang_n'+str(n)+'_type1.out'
    with open(PATH_file) as f:
        lines_str = [line.strip() for line in f]
    lines = []
    for line in lines_str:
        lines.append([int(v) for v in line.strip('} {').split(' ')])

    for k in range(len(lines)):
        triang = lines[k]
        plot_triang_type1(triang,k,n)

# print_type1(4)
print_type1(6)