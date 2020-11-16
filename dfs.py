from SCC import SCC

def dfs1(graph, vertex_id, sequence, debug=False):
    '''The 1st DFS on the reversed graph'''
    dfs_stack = []
    temp_sequence = []

    dfs_stack.append(vertex_id)

    while len(dfs_stack)>0:
        last_vertex_in_stack = dfs_stack.pop()

        if not graph.getGraph()[last_vertex_in_stack].isExplored():

            graph.getGraph()[last_vertex_in_stack].setExplored()
            if debug:
                print('Now vertex {} has been set as explored\n'.format(adjVertex))

            if debug:
                print('The adjecent vertices of {} are:'.format(last_vertex_in_stack))
                print(graph.getGraph()[last_vertex_in_stack].get_adjVertices())

            temp_sequence.append(last_vertex_in_stack)
            if(debug):
                print('vertex {} appended to the temporary sequence'.format(last_vertex_in_stack))

            for adjVertex in graph.getGraph()[last_vertex_in_stack].get_adjVertices():
                if debug:
                    print("Adding vertex {} to the DFS stack".format(adjVertex))
                dfs_stack.append(adjVertex)

    temp_sequence.reverse() #reversing the temporary sequence to maintain the vertices in their order of finishing times
    sequence.extend(temp_sequence) #extending the main sequence list with the reversed temporary sequence


def dfsLoop1(graph,sequence,debug=False):
    '''DFS-loop on reversed graph'''
    global SCCs
    if debug:
        print("\n------------------\nReverse graph")
        print(graph)
    for vertex_id in graph.getGraph():
        if not graph.getGraph()[vertex_id].isExplored():
            if debug:
                print('vertex {} is not yet explored'.format(vertex_id))
            dfs1(graph,vertex_id, sequence, debug)
    if debug:
        print('The sequence of vertices for 2nd DfsLoop on original graph is as follows:')
        print(sequence)


def dfs2(graph, vertex_id, scc ,sequence, debug=False):
    '''The 2st DFS on the original graph'''
    dfs_stack = []
    graph.getGraph()[vertex_id].setExplored()
    dfs_stack.append(vertex_id)

    if debug:
        print("Appended the first vertex of this SCC i.e. the leader vertex {} to the DFS stack\n".format(vertex_id))

    while len(dfs_stack) > 0:
        last_vertex_in_stack = dfs_stack.pop()

        graph.getGraph()[last_vertex_in_stack].updateLeader(scc.getLeader())
        if debug:
            print('The leader of vertex {} has been set to {}\n'.format(last_vertex_in_stack, scc.getLeader()))

        if debug:
            print("Adding the vertex {} to the slave list of {}\n".format(last_vertex_in_stack, scc.getLeader()))
        scc.addSlave(last_vertex_in_stack)

        if debug:
            print('The adjecent vertices of {} are:'.format(last_vertex_in_stack))
            print(graph.getGraph()[last_vertex_in_stack].get_adjVertices())

        for adjVertex in graph.getGraph()[last_vertex_in_stack].get_adjVertices():
            if not graph.getGraph()[adjVertex].isExplored():
                graph.getGraph()[adjVertex].setExplored()
                if debug:
                    print('Now vertex {} has been set as explored\n'.format(adjVertex))
                if debug:
                    print("Appended the vertex {} to the DFS stack".format(adjVertex))
                dfs_stack.append(adjVertex)


def dfsLoop2(graph,SCCs,sequence,debug=False):
    '''DFS-loop on original graph'''
    if debug:
        print("\n------------------\nOriginal graph")
        print(self.__originalGraph.keys())
    for vertex_id in reversed(sequence):
        if not graph.getGraph()[vertex_id].isExplored():
            if debug:
                print('vertex {} is not yet explored'.format(vertex_id))
            leader = vertex_id
            if debug:
                print('Thus the leader is vertex {}'.format(leader))
            scc = SCC(leader, debug)
            dfs2(graph,vertex_id, scc, sequence, debug)
            SCCs.append(scc)
