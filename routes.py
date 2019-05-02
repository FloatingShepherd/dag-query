
# A class represent a collection of routes. 
class Routes:
    def __init__(self, routes):
        self.routes = routes or []

    # Add route of the collection 
    def addRoute(self, route):
        self.routes.append(route)
        return self.routes

    # retunr all routes
    def getRoutes(self):
        return self.routes

    # get length
    def len(self):
        return len(self.routes)

    # get the route with minimum distance
    def getMinDistance(self):
        return min(self.routes, default=None, key=lambda r: r.getDistance())

    # get the route whose last node is the one provided
    def getRoutesEndedWithNode(self, nodeName):
        return Routes([ route for route in self.routes if route.getLastLink().hasChild(nodeName) ])

    # merge two routes
    def merge(self, routes):
        if routes is None:
            return self
        else:
            self.routes = self.routes + routes.getRoutes()
        return self

    # filter routes based on provided filter function
    def filter(self, filterFunc):
        return Routes(list(filter(filterFunc, self.routes)))
