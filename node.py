class Node:
  def __init__(self, name, paths):
    self.name = name
    self.outPaths = paths or []

  def addPath(self, path):
    self.outPaths.append(path)

  def getPaths(self):
    return self.outPaths

  def findPathByChildNode(self, childName):
    return next((path for path in self.outPaths if path.child==childName), None)
  