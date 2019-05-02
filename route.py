from link import Link

# A class represent a path which consists of links. 
# A link is the connection between two nodes, A->B for example. 
# A route looks like A -> B -> C for example.

class Route:
    def __init__(self, links):
        self.links = links or []

    # add an additional link at the end of route.
    def addNextLink(self, link):
        self.links.append(link)
        return self

    # calculate total distance of all links.
    def getDistance(self):
        return sum([link.weight for link in self.links]) if len(self.links) > 0 else None

    # get the link at the end of the route. For A->B->C, it will be B->C.
    def getLastLink(self):
        return self.links[-1]

    # return all links as a collection.
    def getLinks(self):
        return self.links

    # copy/clone links from a different route object.
    def copyFrom(self, route):
        self.links = route.getLinks().copy()
        return self

    # return true when route is going through the provided node
    def hasNode(self, nodeName):
        return next((link for link in self.links if link.parent == nodeName or link.child == nodeName), None) is not None
