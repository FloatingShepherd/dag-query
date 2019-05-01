class route:
    def __init__(self, paths):
        self.paths = paths or []

    def addNextPath(self, path):
        self.paths.append(path)
        return self.paths

    def getDistance(self):
        return sum([path.weight for path in self.paths])

    def getCurrentNode(self):
        return self.paths[-1]
        
