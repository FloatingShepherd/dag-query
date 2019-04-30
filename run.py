from dag import Dag
from node import Node
from path import Path

def getInput():
    return ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']

def generateGraph(input):
    return Dag(generateNodes(input))

def generateNodes(input):
    paths = Path.generatePathsFromArrayInput(input)
    return processPaths(paths, list())

def processPaths(paths, nodes):
    if len(paths) == 0:
        return nodes
    else:
        path = paths[0]
        paths.pop(0)
        nodes = addNodesIfNeeded(path, nodes)
        nodes = addPathToParentNode(path, nodes)
        nodes = processPaths(paths, nodes)
    return nodes

def addNodesIfNeeded(path, nodes):
    parent, child = getParentAndChildNode(path, nodes)
    if parent is None: nodes.append(Node(path.parent, []))
    if child is None: nodes.append(Node(path.child, [])) 
    return nodes

def getParentAndChildNode(path, nodes):
    iterator = (node for node in nodes if node.name==path.parent or node.name==path.child)
    nodeA = next(iterator, None)
    nodeB = next(iterator, None) if nodeA is not None else None

    return nodeA if nodeA is not None and nodeA.name == path.parent else nodeB, nodeA if nodeA is not None and nodeA.name == path.child else nodeB

def addPathToParentNode(path, nodes):
    parent = Dag.findByName(nodes, path.parent)
    parent.addPath(path)
    return nodes

def run():
    dag = generateGraph(getInput())
    
run()
