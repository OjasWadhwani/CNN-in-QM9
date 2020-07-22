import networkx as nx
import numpy as np
import matplotlib as mp
from matplotlib import pyplot as plt
# Keep a list of already added edges in a set edges. Those edges are stored in a frozenset, so already added pairs are not replicated.

# Then build your graph by enumerating the outer list with a starting index of one, then the inner list also with a starting index of one. Zero valued entries are eliminated with the if condition on values:

from collections import defaultdict
from pprint import pprint


inputs = [ [0,1,1,1], [1,0,0,0], [1,0,0,0], [1,0,0,0] ]

def matrixTList(l):

	# l =[[  0.,  15.,   0.,   7.,  10.,   0.],
	#     [ 15.,   0.,   9.,  11.,   0.,   9.],
	#     [  0.,   9.,   0.,   0.,  12.,   7.],
	#     [  7.,  11.,   0.,   0.,   8.,  14.],
	#     [ 10.,   0.,  12.,   8.,   0.,   8.],
	#     [  0.,   9.,   7.,  14.,   8.,   0.]]   

	x, y = np.shape(l)

	outputs = [] 

	for i in range(x):
		for v in range(i + 1, y):
			if(l[i][v]):
				outputs.append([i, v])

	return outputs


pos = np.random.rand(3, 2) #coordinates, (x, y) for 10 nodes
# connect = [tuple(np.random.random_integers(0, 9, size=(2))) for x in range(8)] #random connections

connect = matrixTList(inputs)

print(connect)
print('\n \n')
#creation of the graph
graph = nx.Graph()
#adding nodes/connections in the graph
for node in range(len(pos)):
    graph.add_node(node)
graph.add_edges_from(connect)

#plot of the nodes using the (x,y) pairs as coordinates
graphimg = nx.draw(graph, [(x,y) for x,y in pos], node_size=50)

plt.save('graphimg.png')