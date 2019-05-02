# a node object, which has name and links connect to parent and children. 
# in our design, we only care about children nodes, which are connected by outLinks.
class Node:
  def __init__(self, name, links):
    self.name = name
    self.outLinks = links or []

  # add link going out from the node.
  def addLink(self, link):
    self.outLinks.append(link)

  # return current out going links.
  def getLinks(self):
    return self.outLinks

  # find link by child node name.
  def findLinkByChildNode(self, childName):
    return next((link for link in self.outLinks if link.child==childName), None)
  