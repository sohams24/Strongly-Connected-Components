from Vertex import MyVertex

class MyGraph:
    ''' Object of class MyGraph contains the Graph '''

    def __init__(self, filename,reverse=False,debug=False):
        '''Initialise the graph'''
        self.__graph = {}
        self.__sequence = []
        self.__sccLengths = []
        if debug:
            print('Parsing Graph from File:{}'.format(filename))
        fo = open(filename, 'r')
        # lineNo=0
        for line in fo:
            # lineNo += 1
            line = line.strip()
            line_arr = line.split(' ')

            if not reverse:
                # print(lineNo)
                (root_vertex, slave_vertex) = [x for x in line_arr]
            else:
                (slave_vertex, root_vertex) = [x for x in line_arr]

            #adding root vertex entry to the graph dictonary
            if root_vertex in self.__graph: # Root vertex Entry Already Exists, update the existing entry
                self.__graph[root_vertex].add_adjVertex(slave_vertex)
                if debug:
                    print('To Existing {} in Original. Total_Roots:{}'.format(self.__graph[root_vertex].__str__(), len(self.__graph)))

            else:   #Root vertex entry is new. Add the new root vertex to the dictonary
                self.__graph[root_vertex] = MyVertex(root_vertex)
                self.__graph[root_vertex].add_adjVertex(slave_vertex)

                if debug:
                    print('Newly Created root {} in graph. Total_Roots:{}'.format(self.__graph[root_vertex].__str__(), len(self.__graph)))

            #adding slave vertex entry to the graph dictonary
            if slave_vertex not in self.__graph:
                self.__graph[slave_vertex] = MyVertex(slave_vertex)

                if debug:
                    print('Newly Created root {} in graph. Total_Roots:{}'.format(self.__graph[slave_vertex].__str__(), len(self.__graph)))

        fo.close()


    def getGraph(self):
        return self.__graph
