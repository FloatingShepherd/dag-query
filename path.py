class Path:
    def __init__(self, path):
        self.build(*self.parse(path))

    def parse(self, path):
        return list(path)

    def build(self, parent, child, weight):
        self.parent = parent
        self.child = child
        self.weight = weight

    @staticmethod
    def generatePathsFromArrayInput(input):
        return [Path(p) for p in input if len(p)==3]
  