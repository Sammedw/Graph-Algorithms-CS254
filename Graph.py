from pyvis.network import Network

#Graph data structure using adjacency list
class Graph:

    def __init__(self, nodes=[], edges=[]):
        #Add nodes if provided
        self.adjlist = {}
        if nodes:
            self.adjlist = dict.fromkeys(nodes, [])

        print(self.adjlist)
        #Add edges
        for edge in edges:
            print(edges)
            if edge[0] in nodes and edge[1] in nodes:
                print("ADD")
                self.adjlist[edge[0]].append(edge[1])

    
    def display(self, file="graph.html"):
        net = Network()
        #Add nodes
        net.add_nodes(self.adjlist.keys())
        #Iterate over edges
        for (node, incidentlist) in self.adjlist.items():
            for incident in incidentlist:
                net.add_edge(node, incident)


        net.show(file)


