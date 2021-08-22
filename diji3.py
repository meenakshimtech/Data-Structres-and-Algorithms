
class Node:

    def __init__(self,data,indexloc=None):
        self.data=data
        self.index=indexloc

    
        
 
class Graph:

    @classmethod
    def createfromnode(self,nodes):
        return Graph(len(nodes),len(nodes),nodes)

    def __init__(self,row,col,nodes = None):
        self.adjacencymatrix=[[0] * col for _ in range(row)]
        #print(self.adjacencymatrix)
        self.nodes=nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index=i

    def connectdir(self,node1,node2,weight = 1):
        node1, node2 = self.getindexfromnode(node1),self.getindexfromnode(node2)
        self.adjacencymatrix[node1][node2]=weight


    def connect(self,node1,node2,weight = 1):
        self.connectdir(node1,node2,weight)
        self.connectdir(node2,node1,weight)

    

    def connections_from(self,node):
        node=self.getindexfromnode(node)
        return [(self.nodes[col_num], self.adjacencymatrix[node][col_num]) for col_num in range(len(self.adjacencymatrix[node])) if self.adjacencymatrix[node][col_num] != 0]
        
       
    def dijikstra(self,node):
        nodenum=self.getindexfromnode(node)
        #print(nodeNum)
        
        dist = [None] * len(self.nodes)
        for i in range(len(dist)):
            dist[i]=[float("inf")]
            dist[i].append([self.nodes[nodenum]])

        dist[nodenum][0]=0

        queue = [i for i in range(len(self.nodes))]

        seen = set()
        while len(queue) > 0:
            min_dist = float("inf")
            min_node = None
            for n in queue:
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n
                
            queue.remove(min_node)
            seen.add(min_node)

            connections = self.connections_from(min_node)

            for(node,weight) in connections:
                tot_dist= weight + min_dist
                if tot_dist < dist[node.index][0]:
                    dist[node.index][0]= tot_dist
                    dist[node.index][1]=list(dist[min_node][1])
                    dist[node.index][1].append(node)
        return dist


    def getindexfromnode(self,node):
        
        if not isinstance(node,Node) and not isinstance(node,int):
            raise ValueError('node must be an interger or Node Object')  
        if isinstance(node,int):
            return node
        else:
            return node.index    

  
f=open("inputPS6.txt","r")
f.seek(0)
s=f.readline().rstrip().split(": ")
noofservers=s[1]
f.readline()
nodess=[]
graphvar=[]
uniquewords=[]

for s in f.readlines():
    split_text=s.strip().split(" ")

    if  split_text[0] not in uniquewords:
        uniquewords.append(split_text[0])
    if  split_text[1] not in uniquewords:
        uniquewords.append(split_text[1])
        
for k in sorted(uniquewords):
    if k.isnumeric() == False:
        nodess.append(k)
        s = Node(k)
        graphvar.append(s)

  

graph=Graph.createfromnode(graphvar) 


with open("inputPS6.txt") as tt:
    content = tt.readlines()[2:]
    content = [x for x in content]
    for i in content:
        aa = i.strip()
        bb = aa.split(" ")
        if bb[0] in nodess or bb[1] in nodess:
            graph.connect(graphvar[nodess.index(bb[0])],graphvar[nodess.index(bb[1])],int(bb[2]))



graph.dijikstra(graphvar[0])
x=([(weight, [n.data for  n in node]) for (weight, node) in graph.dijikstra(graphvar[0])])
file1=open('outputPS.txt','w')
for a in x:
    #s=a[1][-1]+a[0]
    if(a[0]!=0):
        file1.write(a[1][-1]+" "+str(a[0])+"\n")
        
file1.close()