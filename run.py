import dagBuilder
from route import Route

# Run all questions.
def run():
    # build graph based on input string array.
    dag = dagBuilder.generateGraph(getInput())

    # 1
    printDistance(dag.getRouteFromString('A-B-C'))
    # 2
    printDistance(dag.getRouteFromString('A-D'))
    # 3
    printDistance(dag.getRouteFromString('A-D-C'))
    # 4
    printDistance(dag.getRouteFromString('A-E-B-C-D'))
    # 5
    printDistance(dag.getRouteFromString('A-E-D'))
    # 6
    printTripCount(dag.findTripsBetweenWithMaxRound('C', 'C', 3))
    # 7
    printTripCount(dag.findTripsBetweenWithExactRound('A', 'C', 4))
    # 8
    printRoute(dag.getShortestDistanceBetweenTwoNodes('A', 'C'))
    # 9
    printRoute(dag.getShortestDistanceBetweenTwoNodes('B', 'B'))
    # 10
    printTripCount(dag.findTripsBetweenWithMaxDistance('C', 'C', 30))

def getInput():
    return ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']

def printError():
    print('NO SUCH ROUTE')

def printRoute(route):
    if route is not None:
        print(route.getDistance())
    else:
        printError()

def printDistance(distance):
    if distance is not None:
        print(distance)
    else:
        printError()

def printTripCount(routes):
    if routes is not None:
        print(routes.len())
    else:
        printError()

run()
