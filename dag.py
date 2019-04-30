class Dag:
    def __init__(self, nodes):
        self.nodes = nodes

    @staticmethod
    def findByName(nodes, name):
        return next((node for node in nodes if node.name==name), None)

    @staticmethod
    def printError():
        print('NO SUCH ROUTE')

    def calculateShortestDistanceBetweenTwoNodes(self, startName, endName):
        startNode = Dag.findByName(self.nodes, startName)
        end = Dag.findByName(self.nodes, endName)
        if start is None or end is None:
            Dag.printError()
        else:
            

    def findChildNode(self, candidateNodePairs, name):
        for c in candidateNodePairs:
            path = c.findPathByChildNode(name)
            if path is not None:
                return path

        newCandidates = set()
        for c in candidates:
            paths = c.getPaths()  
            for p in paths:
                node = findByName(self.nodes, p.child)
                newCandidates.add(node) 
        result = findChildNode(newCandidates, name)
        if result > 0:
            result = result + 