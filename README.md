# Strongly connected components
In this project we find the Strongly Connected Components in a directed social network graph using the "Kosaraju's two-pass algorithm".
Unzip the file "Graph.zip".
The edges of the graph are provided in the text file named "Graph.txt". On every line the first vertex is the start vertex and the second vertex is the end vertex of that edge.
Test cases of small graphs are also provided.
An output file named "SCC.txt" is generated that has all the Strongly connected compenents.

Instructions to run the project:
1)  Clone this repository on your local machine.
2)  Add your input text file to the folder (the graph in your input file should have the format same as the one in "Graph.txt")
3)  Specify the name of your input file in the file "main.py" on line 7.
5)  If you wish to print the debug messages, set the value of 'debug' to 'True' on line 8 in file "main.py" 
6)  Run the file "main.py".
7)  Check the file "SCCs.txt" for the output.

Vertex.py:
This file defines the "Vertex" class.
Every vertex has an "id", a "leader" to indicate the SCC it belongs and a list "adjList" that stores the "ids" of all the vertices adjacent to that vertex.

Graph.py:
This file defines the "Graph" class.
The graph has a dictonary named "graph" which stores all the "Vertex" instances with their respective "ids" as keys.

SCC.py
This file defines the SCC object.
An SCC has a leader vertex named "leader_id", a list of slave vertices named "slavesList" and a counter to maintain the number of vertices in that SCC, named "vertexCount".

dfs.py:
This file defines the different DFS functions to be run on the original and the reverse graphs.

main.py:
This is the file that creates the original and reverse "Graph" instances by passing the input file.
Here we call the "dfsLoop1" and "dfsLoop2" methods on the original and reverse graph instances respectively.

Time Complexity Analysis:
The total time required by this algorithm is the time required to run 2 DFS loops.
Total time required = O(|E|+|V|)