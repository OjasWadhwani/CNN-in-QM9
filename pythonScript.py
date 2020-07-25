from os import listdir
from os.path import isfile, join
import rdkit
from rdkit import Chem
import networkx as nx
import numpy as np
import matplotlib as mp
from matplotlib import pyplot as plt

from collections import defaultdict
from pprint import pprint
import sys
import pandas as pd

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def matrixTList(l):

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


# table = pd.read_csv("")  ######## Make changes here #########

# filesNames = table['']

# files_in_dir = [ f for f in listdir('/home/ojas/sop_qm9/quantum-machine-9-aka-qm9/') if isfile(join('/home/ojas/sop_qm9/quantum-machine-9-aka-qm9/',f)) ]
# # print(files_in_dir[10])



table = pd.read_csv("/home/ojas/Downloads/champs-scalar-coupling/potential_energy.csv")  ######## Make changes here #########

# table.columns
files = table['molecule_name'].to_list()

# files_in_dir = [ f for f in listdir('/home/ojas/sop_qm9/quantum-machine-9-aka-qm9/') if isfile(join('/home/ojas/sop_qm9/quantum-machine-9-aka-qm9/',f)) ]
# prin

counter = 0

for filename in files: 
    
    if(counter >= 0):
        
        coordinates = []

        print(filename+".xyz")

        f = open('/home/ojas/sop_qm9/quantum-machine-9-aka-qm9/' + filename +".xyz", "r")

        i = 0
        flag = 0
        smilesNotation = '\0'
        set = 0

        for l in f:

            # if flag == 1:
            #   flag = flag + 1
            #   continue

            if flag == 1:
                row = l.split('\t')
                smilesNotation = row[0]
                break 

            if i >= 2:
                row = l.split('\t')
                # print("row1: " + row[1])
                if( not(is_number(row[0])) and row[0]!="H" ):
                    if( is_number(row[1]) and is_number(row[2]) ):
                        x = float(row[1])
                        y = float(row[2])
                    else:
                        set = 1
                        break
                    # z = row[3]

                    coordinates.append([x, y])

                elif(row[0] != "H"):
                    flag = 1
                    continue

            i = i + 1

            #   os.system("imageGenerator.py "+smilesNotation+" "+coordinates)
        if set == 1:
            table = table[table.molecule_name != 'dsgdb9nsd_000212']
            continue

        print("smiles: " + smilesNotation)  
        matrix = getMatrix(smilesNotation)
    #     print(matrix)

        pos = coordinates 
    #     print(pos1)
        # print("pos: ")
        # print(pos)

        connect = matrixTList(matrix)
        pos1 = np.random.rand(6, 2)
    #     print(connect)
    #     print(pos)
        #print('\n \n')
        #creation of the graph
        graph = nx.Graph()
        #adding nodes/connections in the graph
        for node in range(len(pos)):
            graph.add_node(node)
        graph.add_edges_from(connect)

        #plot of the nodes using the (x,y) pairs as coordinates
        graphimg = nx.draw(graph, [(x,y) for x,y in pos], node_size=50)

        plt.savefig('/home/ojas/sop_qm9/images/' + filename + '.jpeg')
        plt.show()

    val = table.loc[table['molecule_name'] == filename]
    t = val['potential_energy']
    t = float(t)
    
    df = df.append({'molecule_name': filename, 'potential_energy': t}, ignore_index=True)
    
    print(counter)
    counter = counter + 1

    if counter == 6001:
        break

df.to_csv('/home/ojas/sop_qm9/potential_energy.csv')