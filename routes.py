class Routes:
    def __init__(self, routes):
        self.routes = routes or []

    def addRoute(self, route):
        self.routes.append(route)
        return self.routes

    def getRoutes(self):
        return self.routes

    def getMinDistance(self):
        return min([r.getDistance() for r in self.routes])
        
