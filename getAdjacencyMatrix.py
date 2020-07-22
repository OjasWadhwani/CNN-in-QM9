import rdkit
from rdkit import Chem

def getMatrix(molStr):
    mol = Chem.MolFromSmiles(molStr)
    if not mol:
        print ("Could not create mol for compound")
        return []
    adj = Chem.rdmolops.GetAdjacencyMatrix(mol)
    return adj

print('here')
matrix = getMatrix("[C@H](Cl)(F)Br")
print(matrix)

# def __init__(self):
# 	print('here')
# 	matrix = getMatrix("CCCC")
# 	print(matrix)

