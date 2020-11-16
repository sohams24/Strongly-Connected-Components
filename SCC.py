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

    def getSlavesList(self):
        return self.__slavesList

    def __str__(self):
        str1 = format("Leader: {}........vertex count: {}".format(self.getLeader(), self.getSCCLength()))
        # str1 += "\nList of vertices : "
        # for vertex in self.__slavesList:
        #     str1 += str(vertex) + " "
        str1 += "\n"
        return str1
