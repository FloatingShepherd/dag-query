# DAG class, which contains a collection of nodes. 
# This class also contains methods used to do query.

from routes import Routes
from route import Route
from functools import partial
class Dag:
    def __init__(self, nodes):
        self.nodes = nodes

    # find node by name (static method)
    @staticmethod    
    def findByNameStatic(nodes, name):
        return next((node for node in nodes if node.name==name), None)

    # filter function based on max distance
    @staticmethod
    def distanceLessThanFilter(route, distance):
        return route.getDistance() < distance

    # find node by name
    def findByName(self, name):
        return next((node for node in self.nodes if node.name==name), None)

    # generate a route based on string input, 'A->B->C' for example.
    def getRouteFromString(self, routeString):   
        nodes = [self.findByName(n) for n in routeString.split('-')]
        return self.getRouteBasedOnNodes(nodes)

    # generate a route based on provided nodes (in sequence).
    # return None when nodes are not connected.
    def getRouteBasedOnNodes(self, nodes):
        if len(nodes) <= 1:
            return 0
        else: 
            link = nodes[0].findLinkByChildNode(nodes[1].name)
            if link is None:
                return None
            else:
                nodes.pop(0)
                distance = self.getRouteBasedOnNodes(nodes)
                return link.weight + distance if distance is not None else None

    # find shortest distance between two nodes.
    # return None when not connected.
    def getShortestDistanceBetweenTwoNodes(self, startName, endName):
        startNode = self.findByName(startName)
        endNode = self.findByName(endName)
        if startNode is None or endNode is None:
            return None
        else:
            return self.findShortestRoute(startNode, endName)

    def findShortestRoute(self, startNode, destinationName):
        # get routes to process by getting all out going links of the starting node
        candidateRoutes = Routes([Route([link]) for link in startNode.getLinks()])
        minRoute = None

        # candiate routes are the routes to process. 
        # they can be empty when no more routes can have distances less than the current minimum distance
        # or cannot find any more routes
        while candidateRoutes.len() > 0:
            # finished routes store the routes connecting start node and end node
            finishedRoutes = candidateRoutes.getRoutesEndedWithNode(destinationName)
            _minRoute = finishedRoutes.getMinDistance()
            minRoute = _minRoute if minRoute is None or (_minRoute is not None and minRoute.getDistance() > _minRoute.getDistance()) else minRoute

            # filter out routes having bigger distance than min route
            candidateRoutes = Routes([route for route in candidateRoutes.getRoutes() if minRoute is None or route.getDistance() < minRoute.getDistance()])
            # all candidate routes go one step further. Store the new generated routes 
            candidateRoutes = Routes([Route([]).copyFrom(route).addNextLink(link) \
                            for route in candidateRoutes.getRoutes() for link in self.findByName(route.getLastLink().child).getLinks() \
                            if not route.hasNode(link.child) or (link.child == destinationName and startNode.name == destinationName)])

        return minRoute

    # find trips between two nodes with the constraint of max round of interation.
    # return None when not found.
    def findTripsBetweenWithMaxRound(self, startName, endName, maxRound):
        startNode = self.findByName(startName)
        endNode = self.findByName(endName)
        if startNode is None or endNode is None:
            return None
        else:
            return self.findRoutesWithMaxRound(startNode, endName, maxRound)  

    def findRoutesWithMaxRound(self, startNode, destinationName, maxRound):
        # get routes to process by getting all out going links of the starting node
        candidateRoutes = Routes([Route([link]) for link in startNode.getLinks()])
        count = 0
        finishedRoutes = None

        while candidateRoutes.len() > 0 and maxRound is not None and count < maxRound:
            # finished routes store the routes connecting start node and end node
            finishedRoutes = candidateRoutes.getRoutesEndedWithNode(destinationName).merge(finishedRoutes)
            # all candidate routes go one step further. Store the new generated routes 
            candidateRoutes = Routes([Route([]).copyFrom(route).addNextLink(link) \
                                for route in candidateRoutes.getRoutes() for link in self.findByName(route.getLastLink().child).getLinks()])
            count = count + 1

        return finishedRoutes

    # find trips between two nodes with the constraint of exact round of interation.
    # return None when not found.
    def findTripsBetweenWithExactRound(self, startName, endName, round):
        startNode = self.findByName(startName)
        endNode = self.findByName(endName)
        if startNode is None or endNode is None:
            return None
        else:
            return self.findRoutesWithExactRound(startNode, endName, round)  

    def findRoutesWithExactRound(self, startNode, destinationName, round):
        # get routes to process by getting all out going links of the starting node
        candidateRoutes = Routes([Route([link]) for link in startNode.getLinks()])
        count = 0
        finishedRoutes = None

        while candidateRoutes.len() > 0 and round is not None and count < round:
            if count + 1 == round:
                # finished routes store the routes connecting start node and end node
                finishedRoutes = candidateRoutes.getRoutesEndedWithNode(destinationName).merge(finishedRoutes)
            # all candidate routes go one step further. Store the new generated routes 
            candidateRoutes = Routes([Route([]).copyFrom(route).addNextLink(link) \
                                for route in candidateRoutes.getRoutes() for link in self.findByName(route.getLastLink().child).getLinks()])
            count = count + 1

        return finishedRoutes

    # find trips between two nodes with the constraint of max distance.
    # return None when not found.
    def findTripsBetweenWithMaxDistance(self, startName, endName, distance):
        startNode = self.findByName(startName)
        endNode = self.findByName(endName)
        if startNode is None or endNode is None:
            return None
        else:
            return self.findRoutesWithMaxDistance(startNode, endName, distance)  

    def findRoutesWithMaxDistance(self, startNode, destinationName, distance):
        # get routes to process by getting all out going links of the starting node
        candidateRoutes = Routes([Route([link]) for link in startNode.getLinks()])
        finishedRoutes = None
        # define filter function with partial function
        lessThanFilterFunc = partial(Dag.distanceLessThanFilter, distance=distance)
        while candidateRoutes.len() > 0:
            # finished routes store the routes connecting start node and end node
            finishedRoutes = candidateRoutes.getRoutesEndedWithNode(destinationName).filter(lessThanFilterFunc).merge(finishedRoutes)
            # all candidate routes go one step further. Store the new generated routes 
            candidateRoutes = Routes([Route([]).copyFrom(route).addNextLink(link) \
                                for route in candidateRoutes.getRoutes() for link in self.findByName(route.getLastLink().child).getLinks()])
            # filter out routes having more distance than the max distance
            candidateRoutes = Routes([route for route in candidateRoutes.getRoutes() if route.getDistance() < distance])

        return finishedRoutes
