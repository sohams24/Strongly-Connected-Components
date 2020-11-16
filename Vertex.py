class MyVertex:
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

    def get_adjVertices(self):
        return self.__adjList[:]

    def add_adjVertex(self, vertex_id):
        self.__adjList.append(vertex_id)

    def isExplored(self):
        return self.__isExplored

    def setExplored(self):
        self.__isExplored = True

    def __str__(self):
        str1 = format("Root_vertex:{}   Leader:{}   Adjecent vertices:{}".format(self.get_id(), self.__leader, self.__adjList))
        return str1
