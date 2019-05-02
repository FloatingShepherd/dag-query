# a link connects two nodes. A -> B e.g.

class Link:
    def __init__(self, link):
        self.build(*self.parse(link))

    # generate links based on string input, [AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7] for example.
    @staticmethod
    def generateLinksFromArrayInput(input):
        return [Link(i) for i in input if len(i)==3]

    # parse string like AB5 to an array ['A', 'B'. '5']
    def parse(self, link):
        return list(link)

    # assign values
    def build(self, parent, child, weight):
        self.parent = parent
        self.child = child
        self.weight = int(weight)

    # return true if link has child as provided name
    def hasChild(self, name):
        return self.child == name
  