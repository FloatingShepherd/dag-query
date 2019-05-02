# this file contains functions used to build DAG. 
# logic flow starts from generateGraph.

from dag import Dag
from node import Node
from link import Link

def generateGraph(input):
    return Dag(generateNodes(input))

def generateNodes(input):
    links = Link.generateLinksFromArrayInput(input)
    return processLinks(links, list())

def processLinks(links, nodes):
    if len(links) == 0:
        return nodes
    else:
        link = links[0]
        links.pop(0)
        nodes = addNodesIfNeeded(link, nodes)
        nodes = addLinkToParentNode(link, nodes)
        nodes = processLinks(links, nodes)
    return nodes

def addNodesIfNeeded(link, nodes):
    parent, child = getParentAndChildNode(link, nodes)
    if parent is None: nodes.append(Node(link.parent, []))
    if child is None: nodes.append(Node(link.child, [])) 
    return nodes

def getParentAndChildNode(link, nodes):
    iterator = (node for node in nodes if node.name==link.parent or node.name==link.child)
    nodeA = next(iterator, None)
    nodeB = next(iterator, None) if nodeA is not None else None

    return nodeA if nodeA is not None and nodeA.name == link.parent else nodeB, nodeA if nodeA is not None and nodeA.name == link.child else nodeB

def addLinkToParentNode(link, nodes):
    parent = Dag.findByNameStatic(nodes, link.parent)
    parent.addLink(link)
    return nodes
