# Strongly connected components
In this project we find the Stronglu Connected Components in a directed graph using Kosaraju's two-pass algorithm.
The edges of the graph are provided in a text file named "Graph.txt". On every line the first vertex is the start vertex and the second vertex is the end vertex of that edge.
Test cases of small graphs are also provided.
An output file named "SCC.txt" is generated that has all the Strongly connected compenents.

Instructions to run the project:
1)  Clone this repository on your local machine.
2)  Add your input text file to the folder (the graph in your input file should have the format same as the one in "Graph.txt")
3)  Specify the name of your input file in the file "main.py" on line 7.
4)  Set the number of iterations you wish to run in file "main.py" on line 11.
5)  If you wish to print the debug messages, set the value of 'debug' to 'True' on line 6 in file "main.py" 
6)  Run the file "main.py".
7)  Check the file "minCutOutput.txt" for the output.

Vertex.py:
This file defines the "Vertex" class.
Every vertex has an "id" and a set "edgeSet" that stores all the "ids" of all the edges incident to that vertex.

Edge.py:
This file defines the "Edge" class.
Every edge has an "id" and two end vertices named "v1" and "v2".

Graph.py:
This file defines the "Graph" class.
The graph has two dictonaries named "vertexDict" and "edgeDict".
"vertexDict" stores all the "Vertex" instances with their respective "ids" as keys.
"edgeDict" stores all the "Edge" instances with their respective "ids" as keys.
The method "karger" computes the min-cut.

kargerMinCut.py:
This is the file that creates the "Graph" instance by passing the input file.
Here we call the "karger" method from the graph instance.
The Karger's algorithm does not gurrantee to give the correct result in a single iteration.
Thus we run multiple iterations of the algorithm and choose the result that gives minimum number of edges in the min-cut.

Time Complexity Analysis:
Whenevere we contract an edge, we are changing the end vertex for all incident edges of one of the vertices (the vertex that gets deleted) of the contracted edge.
We repeat this process n-2 times, where n=|V|. Thus total number of operations performed is proportional to the sum of the degrees of those n-2 vertices.
Sum of the degrees of all vertices is twice the number of edges.
Time comlplexity for one iteration: O(m) where m=|E|
Overall time complexity for N iterations: O(N x m) where N=number of iterations performed.


# Strongly Connected Components
Compute the strongly connected components of a given directed graph using Kosaraju's 2 pass algorithm. (Stack Implementation)

Different test cases are provided.
To run the code on the actual dataset, unzip the file SCC.zip and pass it as input.
