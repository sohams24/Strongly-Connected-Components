SCCs = []

class MyNode:
    '''Contains the Structure of vertex elements'''

    def __init__(self, my_id=None, adjList=None, leader=None):

        if adjList:
            self.__adjList = adjList
        else:
            self.__adjList = []

        self.__myid = my_id

        if leader:
            self.__leader = leader
        else:
            self.__leader = self.__myid

        self.__isExplored = False

    def get_id(self):
        return self.__myid

    def updateLeader(self, leader=None):
        if leader:
            self.__leader = leader
        else:
            self.__leader = self

    def get_adjNodes(self):
        return self.__adjList[:]

    def add_adjNode(self, vertex_id):
        self.__adjList.append(vertex_id)

    def checkIfExplored(self):
        return self.__isExplored

    def setExplored(self):
        self.__isExplored = True

    def __str__(self):
        str1 = format("Root_vertex:{}   Leader:{}   Adjecent vertices:{}".format(self.get_id(), self.__leader, self.__adjList))
        return str1



class MyGraph:
    ''' Object of class MyGraph contains the Graph '''

    def __init__(self, filename, debug=False):
        '''Initialise the graph'''
        self.__originalGraph = {}
        self.__reverseGraph = {}
        self.__sequence = []
        self.__sccLengths = []
        if debug:
            print('Parsing Graph from File:{}'.format(filename))
        fo = open(filename, 'r')
        for line in fo:
            line = line.strip()
            line_arr = line.split(' ')
            (root_vertex, slave_vertex) = [int(x, 10) for x in line_arr]

            #adding root vertex entry to the original graph dictonary
            if root_vertex in self.__originalGraph.keys(): # Root vertex Entry Already Exists, update the existing entry
                self.__originalGraph[root_vertex].add_adjNode(slave_vertex)
                if debug:
                    # pass
                    print('To Existing {} in Original. Total_Roots:{}'.format(self.__originalGraph[root_vertex].__str__(), len(self.__originalGraph.keys())))
            else:   #Root vertex entry is new. Add the new root vertex to the dictonary
#                 self.__originalGraph[root_vertex] = MyNode(root_vertex)
                self.__originalGraph.update({root_vertex:MyNode(root_vertex)})
#                 self.__originalGraph.update({root_vertex:None})
#                 self.__originalGraph[root_vertex] = MyNode(root_vertex)
                self.__originalGraph[root_vertex].add_adjNode(slave_vertex)
                if debug:
                    # pass
                    print('To Newly Created {} in Original. Total_Roots:{}'.format(self.__originalGraph[root_vertex].__str__(), len(self.__originalGraph.keys())))

            #adding slave vertex entry to the original graph dictonary
            if slave_vertex not in self.__originalGraph.keys():
                self.__originalGraph.update({slave_vertex:MyNode(slave_vertex)})
                if debug:
                    # pass
                    print('To Newly Created {} in Original. Total_Roots:{}'.format(self.__originalGraph[slave_vertex].__str__(), len(self.__originalGraph.keys())))

            #adding slave vertex entry to the reverse graph dictonary
            if slave_vertex in self.__reverseGraph.keys(): # slave vertex Entry Already Exists
                self.__reverseGraph[slave_vertex].add_adjNode(root_vertex)
                if debug:
                    pass
                    print('To Existing {} in Reverse. Total_Roots:{}'.format(self.__reverseGraph[slave_vertex].__str__(), len(self.__reverseGraph.keys())))
            else:   #Slave vertex entry is new. Add the new slave vertex to the dictonary
                self.__reverseGraph.update({slave_vertex:MyNode(slave_vertex)})
                self.__reverseGraph[slave_vertex].add_adjNode(root_vertex)
                if(debug):
                    pass
                    print('To Newly Created {} in Reverse. Total_Roots:{}'.format(self.__reverseGraph[slave_vertex].__str__(), len(self.__reverseGraph.keys())))

            #adding root vertex entry to the reverse graph dictonary
            if root_vertex not in self.__reverseGraph.keys():
                self.__reverseGraph.update({root_vertex:MyNode(root_vertex)})
                if(debug):
                    pass
                    print('To Newly Created {} in Reverse. Total_Roots:{}'.format(self.__reverseGraph[root_vertex].__str__(), len(self.__reverseGraph.keys())))

        fo.close()


    def dfs(self, vertex_id, scc , reverse=False, debug=False):
        '''The DFS subroutine'''
        dfs_stack = []
        temp_sequence = []
        if reverse:
            self.__reverseGraph[vertex_id].setExplored()
            dfs_stack.append(vertex_id)

            while len(dfs_stack)>0:
                last_vertex_in_stack = dfs_stack.pop()

                if debug:
                    print('The adjecent vertices of {} are:'.format(last_vertex_in_stack))
                    print(self.__reverseGraph[last_vertex_in_stack].get_adjNodes())

                temp_sequence.append(last_vertex_in_stack)
                if(debug):
                    print('vertex {} appended to the temporary sequence'.format(last_vertex_in_stack))
                for adjNode in self.__reverseGraph[last_vertex_in_stack].get_adjNodes():
                    if not self.__reverseGraph[adjNode].checkIfExplored():
                        self.__reverseGraph[adjNode].setExplored()
                        if debug:
                            print('Now vertex {} has been set as explored\n'.format(adjNode))
                        if debug:
                            print("Adding vertex {} to the DFS stack".format(adjNode))
                        dfs_stack.append(adjNode)
            temp_sequence.reverse() #reversing the temporary sequence to maintain the vertices in their order of finishing times
            self.__sequence.extend(temp_sequence) #extending the main sequence list with the reversed temporary sequence

            # for adjNode in self.__reverseGraph[vertex_id].get_adjNodes():
            #     if not self.__reverseGraph[adjNode].checkIfExplored():


                    # self.dfs(adjNode, leader, None, reverse, debug)

        else:
            self.__originalGraph[vertex_id].setExplored()
            dfs_stack.append(vertex_id)
            if debug:
                print("Appended the first vertex of this SCC i.e. the leader vertex {} to the DFS stack\n".format(vertex_id))
            while len(dfs_stack) > 0:

                last_vertex_in_stack = dfs_stack.pop()

                # self.__originalGraph[last_vertex_in_stack].setExplored()
                # if debug:
                #     print('Now vertex {} has been set as explored\n'.format(last_vertex_in_stack)

                self.__originalGraph[last_vertex_in_stack].updateLeader(scc.getLeader())
                if debug:
                    print('The leader of vertex {} has been set to {}\n'.format(last_vertex_in_stack, scc.getLeader()))

                if debug:
                    print("Adding the vertex {} to the slave list of {}\n".format(last_vertex_in_stack, scc.getLeader()))
                scc.addSlave(last_vertex_in_stack)

                if debug:
                    print('The adjecent vertices of {} are:'.format(last_vertex_in_stack))
                    print(self.__originalGraph[last_vertex_in_stack].get_adjNodes())

                for adjNode in self.__originalGraph[last_vertex_in_stack].get_adjNodes():
                    if not self.__originalGraph[adjNode].checkIfExplored():
                        self.__originalGraph[adjNode].setExplored()
                        if debug:
                            print('Now vertex {} has been set as explored\n'.format(adjNode))
                        if debug:
                            print("Appended the vertex {} to the DFS stack".format(adjNode))
                        dfs_stack.append(adjNode)


    def dfsLoop(self, reverse=False, debug=False):
        '''DFS-loop subroutine'''
        global SCCs
        if reverse:
            if debug:
                print("\n------------------\nReverse graph")
                print(self.__reverseGraph.keys())
            for vertex_id in self.__reverseGraph.keys():
                if not self.__reverseGraph[vertex_id].checkIfExplored():
                    if debug:
                        print('vertex {} is not yet explored'.format(vertex_id))
                    self.dfs(vertex_id, None, reverse, debug)
            if debug:
                print('The sequence of vertices for 2nd DfsLoop on original graph is as follows:')
                print(self.__sequence)

        else:
            if debug:
                print("\n------------------\nOriginal graph")
                print(self.__originalGraph.keys())
            for vertex_id in reversed(self.__sequence):
                if not self.__originalGraph[vertex_id].checkIfExplored():
                    if debug:
                        print('vertex {} is not yet explored'.format(vertex_id))
                    leader = vertex_id
                    if debug:
                        print('Thus the leader is vertex {}'.format(leader))
                    scc = SCC(leader, debug)
                    self.dfs(vertex_id, scc, reverse, debug)
                    SCCs.append(scc)


    def __str__(self):
        str2 = '\nOriginal graph is as follows\n'
        str2 += '-'*52 + '\n'
        for vertex_id, vertexObject in self.__originalGraph.items():
            str2 += '\n{}'.format(vertexObject.__str__())
        str2 += '-'*52 + '\n'
        str2 += '\nReverse graph is as follows\n'
        str2 += '-'*52 + '\n'
        for vertex_id,vertexObject in self.__reverseGraph.items():
            str2 += '\n{}'.format(vertexObject.__str__())
        str2 += '-'*52 + '\n'
        return str2


class SCC:
    '''Object of this class is an SCC'''

    def __init__(self, leader, debug=False):
        '''Initialises the parameters of the SCC'''
        if debug:
            print("Initialising the SCC object!")
        self.__leader_id = leader
        self.__vertexCount = 0
        self.__slavesList = []

    def getLeader(self):
        return self.__leader_id

    def addSlave(self, slave_vertex_id):
        '''Appends the slaves list by the vertex id in the arguments'''
        self.__slavesList.append(slave_vertex_id)
        self.__vertexCount += 1

    def getSCCLength(self):
        return self.__vertexCount

    def getSCC(self):
        return (__leader_id, __slavesList)

    def __str__(self):
        str1 = format("Leader: {}........vertex count: {}".format(self.getLeader(), self.getSCCLength()))
        # str1 += "\nList of vertices : "
        # for vertex in self.__slavesList:
        #     str1 += str(vertex) + " "
        str1 += "\n"
        return str1


g1 = MyGraph('SCC.txt', debug=False)
g1.dfsLoop(reverse=True, debug=False)
g1.dfsLoop(reverse=False, debug=False)
# print(g1)
SCCs.sort(key=lambda x: x.getSCCLength(), reverse=True)
for i in range(5):
    print(SCCs[i])
