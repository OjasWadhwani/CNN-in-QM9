# from getAdjacencyMatrix import getMatrix
# from getGraph import

x = 76
# str(x).zfill(6)
# print(x)
print("dsgdb9nsd_" + str(x).zfill(6) + ".xyz")

f = open("quantum-machine-9-aka-qm9/dsgdb9nsd_" + str(x).zfill(6) + ".xyz", "r")
# count = 0
# for line in f:
# 	for i in line: 
# 		if i == "\n":
# 			count = count + 1
# print (count)
# atoms = int(f.readline());
# print(atoms)
# for line in range(3, atoms+2):
# 	print()
# print(f.readlines(atoms))

l = f.readlines();
print(l);

atoms = l[0];
print(atoms)






f.close()