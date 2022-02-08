graph=dict()
graph['A']=['B','C']
graph['B']=['E','A']
graph['C']=['A','B','E','F']
graph['E']=['B','C']
graph['F']=['C']
#by using a adjcncy matrix 
matrix_elements= sorted(graph.keys())
cols=rows=len(matrix_elements)#len is to provide the length of the columns and rows
adjmatrix=[[0 for x in range(rows)] for y in range(cols)]
edges_list=[0]#l will be stored as tuples
for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key,neighbor))  
for edge in edges_list:
    index_of_first_matrix=matrix_elements.index(edge[0])
    index_of_second_matrix=matrix_elements.index(edge[1])
    adjmatrix[index_of_first_matrix][index_of_second_matrix]=1