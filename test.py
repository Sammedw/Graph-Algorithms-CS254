from pyvis.network import Network

G =  Network()

G.add_nodes(["a", "b", "c"])

G.show("test.html")