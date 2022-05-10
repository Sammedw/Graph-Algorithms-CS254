from pyvis.network import Network

#Graph data structure using adjacency list
class Graph:

    def __init__(self, nodes=[], edges=[]):
        #Add nodes if provided
        self.adjlist = {}
        if nodes:
            self.adjlist = dict.fromkeys(nodes, [])

        #Add edges
        for edge in edges:
            if edge[0] in nodes and edge[1] in nodes:
                self.adjlist[edge[0]].append(edge[1])

    
    def display(self):
        net = Network()
        #Add nodes
        net.add_nodes(self.adjlist.keys())
        #Iterate over edges
        for node in self.adjlist.keys():
            for edge in 


