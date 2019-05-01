class Node:
  def __init__(self, name, links):
    self.name = name
    self.outLinks = links or []

  def addLink(self, link):
    self.outLinks.append(link)

  def getLinks(self):
    return self.outLinks

  def findLinkByChildNode(self, childName):
    return next((link for link in self.outLinks if link.child==childName), None)
  