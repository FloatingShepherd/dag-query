import dagBuilder

def getInput():
    return ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']

def run():
    dag = dagBuilder.generateGraph(getInput())
    
run()
