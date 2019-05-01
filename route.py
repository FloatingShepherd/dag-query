class Route:
    def __init__(self, links):
        self.links = links or []

    def addNextLink(self, link):
        self.links.append(link)
        return self.links

    def getDistance(self):
        return sum([link.weight for link in self.links])

    def getCurrentNode(self):
        return self.links[-1]

    def getLinks(self):
        return self.links

    def copyFrom(self, route):
        self.links = route.getLinks()
        
