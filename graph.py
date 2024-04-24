graph=[(1,2,5),(2,3,4),(3,4,10),(4,5,6),(1,3,9),(2,4,6),(3,5,8)]
vertexset=set()
td=0
for edge in graph:
    print(edge)
    vertexset.add(edge[0])
    vertexset.add(edge[1])
    td=td+edge[2]
print("total distance of the graph is:",td)
print("no of the vertes=",len(vertexset))
print("no of the edges=",len(graph))
print("sorted graph based on distance",graph)
print(graph)



#adjaceny matrix
graph=[(1,2,5),(2,3,4),(3,4,10),(4,5,6),(1,3,9),(2,4,6),(3,5,8)]
vertexset=set()
adj_mat=[]
for edge in graph:
    vertexset.add(edge[0])
    vertexset.add(edge[1])
nv=len(vertexset)
print(nv)
adj_mat=[[0]*nv for i in range(nv)]
for row in adj_mat:
    print(row)
for edge in graph:
    adj_mat[edge[0]-1][edge[1]-1]=edge[2]
    adj_mat[edge[1]-1][edge[0]-1]=edge[2]
print("adj matrix")
for row in adj_mat:
    print(row)

    
    
