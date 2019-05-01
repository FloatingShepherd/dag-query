class Link:
    def __init__(self, link):
        self.build(*self.parse(link))

    @staticmethod
    def generateLinksFromArrayInput(input):
        return [Link(i) for i in input if len(i)==3]
        
    def parse(self, link):
        return list(link)

    def build(self, parent, child, weight):
        self.parent = parent
        self.child = child
        self.weight = weight

  