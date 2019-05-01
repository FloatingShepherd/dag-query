from routes import Routes
from route import Route

class Dag:
    def __init__(self, nodes):
        self.nodes = nodes

    @staticmethod    
    def findByName(nodes, name):
        return next((node for node in nodes if node.name==name), None)

    def findByName(self, name):
        return next((node for node in self.nodes if node.name==name), None)

    def getShortestDistanceBetweenTwoNodes(self, startName, endName):
        startNode = findByName(startName)
        endNode = findByName(endName)
        if startNode is None or endNode is None:
            Dag.printError()
        else:
            routes = Routes([Route(startNode.getLinks())])
            findChildNode(endName, routes, Route())

    def hasShorterRoute(routes, route):
        return min([r.getDistance()  for r in routes]) < route.getDistance()

    def findChildNode(self, destinationName, candidateRoutes, minRoute):
        newRoutes = Routes()
        
        for route in candidateRoutes.getRoutes():
            lastNode = route.getCurrentNode()
            link = lastNode.findLinkByChildNode(destinationName)
            if link is not None:
                route.addNextLink(link)
                minRoute.copyFrom(returnMinRoute(minRoute, route))
            else:
                links = lastNode.getLinks()
                for l in links:


        Dag.hasShorterRoute(candidateRoutes, route)
        newCandidates = set()
        for c in candidates:
            links = c.getLinks()  
            for link in links:
                node = findByName(self.nodes, link.child)
                newCandidates.add(node) 
        result = findChildNode(newCandidates, destinationName)
        if result > 0:
            result = result + 

    def returnMinRoute(self, currentMinRoute, route):
        return currentMinRoute if currentMinRoute.getDistance() < route.getDistance() else route

    def printError(self):
        print('NO SUCH ROUTE')
    