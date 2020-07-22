import rdkit
from rdkit import Chem
import networkx as nx
import numpy as np
import matplotlib as mp
from matplotlib import pyplot as plt

from collections import defaultdict
from pprint import pprint

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

def getMatrix(molStr):
    mol = Chem.MolFromSmiles(molStr)
    if not mol:
        print ("Could not create mol for compound")
        return []
    adj = Chem.rdmolops.GetAdjacencyMatrix(mol)
    return adj

#print('here')
matrix = getMatrix(argv[1])
#print(matrix)

pos = argv[2] #np.random.rand(3, 2) #coordinates, (x, y) for 10 nodes
# connect = [tuple(np.random.random_integers(0, 9, size=(2))) for x in range(8)] #random connections

connect = matrixTList(matrix)

#print(connect)
#print('\n \n')
#creation of the graph
graph = nx.Graph()
#adding nodes/connections in the graph
for node in range(len(pos)):
    graph.add_node(node)
graph.add_edges_from(connect)

#plot of the nodes using the (x,y) pairs as coordinates
graphimg = nx.draw(graph, [(x,y) for x,y in pos], node_size=50)

plt.save(argv[1]+'.png')

# def __init__(self):
# 	print('here')
# 	matrix = getMatrix("CCCC")
# 	print(matrix)
