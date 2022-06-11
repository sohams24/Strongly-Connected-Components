from Graph import MyGraph
from dfs import dfs1
from dfs import dfsLoop1
from dfs import dfs2
from dfs import dfsLoop2

filename = 'Graph.txt'
debug = False
graph = MyGraph(filename,False, debug)
reverse_graph = MyGraph(filename, True, debug)
sequence = list()
dfsLoop1(reverse_graph,sequence,debug)
SCCs = list()
dfsLoop2(graph,SCCs,sequence,debug)
# SCCs.sort(key=lambda x: x.getSCCLength(), reverse=True)
f = open('SCCs.txt','w')
f.write("Following are the strongly connected components for graph {}.\n".format(filename))
for scc in SCCs:
    f.write("[")
    for i in range(scc.getSCCLength()):
        f.write("{}".format(scc.getSlavesList()[i]))
        if i == scc.getSCCLength()-1:
            f.write("]\n")
        else:
            f.write(", ")
    f.write("No of vertices: {}\n\n\n".format(scc.getSCCLength()))
f.close()
print("Check the file 'SCCs.txt' for the strongly connected compenents ")


