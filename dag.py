from functools import partial

class Dag:
    def __init__(self, nodes):
        self.nodes = nodes

    @staticmethod
    def findByName(nodes, name):
        return next((node for node in nodes if node.name==name), None)

    @staticmethod
    def printError():
        print('NO SUCH ROUTE')

    def getShortestDistanceBetweenTwoNodes(self, startName, endName):
        startNode = Dag.findByName(self.nodes, startName)
        end = Dag.findByName(self.nodes, endName)
        if start is None or end is None:
            Dag.printError()
        else:
            routesFound = [] 
            addRoute = partial(Dag.foundRoute, routesFound)

            findChildNode([Route(startNode.getPaths())], endName, addRoute)

    @staticmethod        
    def foundRoute(routesFound, route):
        routesFound.append(route)
        return  routesFound

    def hasShorterRoute(routes, route):
        return min([r.getDistance()  for r in routes]) < route.getDistance()

    def findChildNode(self, candidateRoute, name, addRoute):
        for route in candidateRoute:
            lastNode = route.getCurrentNode()
            path = lastNode.findPathByChildNode(name)
            if path is not None:
                route.addNextPath(path)
                addRoute(route)

        newCandidates = set()
        for c in candidates:
            paths = c.getPaths()  
            for p in paths:
                node = findByName(self.nodes, p.child)
                newCandidates.add(node) 
        result = findChildNode(newCandidates, name)
        if result > 0:
            result = result + 

    