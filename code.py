import numpy as np
import pandas as pd
import pylon
import matplotlib.pyplot
import random
import csv


# first 100,000 records
input_file = "train_subset.csv"

# comma delimited is the default, set data type to unicode
df = pd.read_csv(input_file, header = 0, dtype="unicode")
# put the original column names in a python list
original_headers = list(df.columns.values)

# create a numpy array
numpy_array = df.as_matrix()

# delete records not needed
strip_numpy_array = np.delete(numpy_array, [0,2,3,4,5,7,8,9,10,14,15,16,17,18,19,20,21,22,23], axis=1)

# remove records of non-clicked activity by using boolean to check each element for where there's a "0"
clk_conversions = strip_numpy_array[np.logical_not(strip_numpy_array[:,0] == "0")]


# [0] click, [1] site domain, [2] device id, [3] device ip, [4] device model
# create node array for nodes.csv
node = np.delete(clk_conversions, [0], axis=1)
# create edge array for edges.csv, but keep site domain
edge = np.delete(clk_conversions, [0], axis=1)
# empty dataset 
nodes_out = []
uniq_nodes_out = []
edges_out = []

# node & edge - [0] site_domain , [1] device id , [2] device ip, [3] device model
# combine device ip + device model for rows that appear to not have unique device model
for i in node:
    if i[1] == "a99f214a":
        # concat two hashed values
        concat = i[2]+i[3]
        node_hashed = np.append(i, concat)
        # delete rows no longer needed that do not identify unique user
        add_nodes = np.delete(node_hashed, [0,1,2,3], axis=0)
    else:
        # include rows as normal, nothing to be done here
        add_nodes = np.delete(i, [0,2,3], axis=0) 
    nodes_out.append(add_nodes)
    nodes = np.array(nodes_out)
# print only unique entries - no duplicates
unique_nodes = np.unique(nodes)
        
for i in edge:
    if i[1] == "a99f214a":
        concat = i[2]+i[3]
        edge_hashed = np.append(i, concat)
        # delete rows for edges
        add_edges = np.delete(edge_hashed, [1,2,3], axis=0)
    else:
        # include rows as normal, nothing to be done here
        add_edges = np.delete(i, [2,3], axis=0)
    # reverse array for gephi formatting (source, target)
    reversed_edges = np.flipud(add_edges)
    edges_out.append(reversed_edges)
    edges = np.array(edges_out)

# save new + modified dataset into csv 
np.savetxt("nodes.csv", unique_nodes, fmt="%s", delimiter=",", header="Id, Label", comments='')
np.savetxt("edges.csv", edges, fmt="%s", delimiter=",", header="Source,Target", comments='')


# General code generate graphs (Degree vs Betweenness Example)

file_name = ('/Users/thsolo/ctr_network/w5.csv')

np.set_printoptions(suppress=True)
csv = np.genfromtxt (file_name, delimiter=",", dtype=float)
y = csv[1:,1]
x =  csv[1:,2]

# set limits for the axes
plt.gca().set_ylim([0.9,100000])
plt.gca().set_xlim([0.9,100000000])
 
# log-log plot
plt.gca().set_xscale("log")
plt.gca().set_yscale("log")

# label axis
plt.xlabel('Degree (k)', fontsize=10)
plt.ylabel('Betweeness Centrality', fontsize=10)

plt.plot(x, y, 'ro')
plt.show()


