'''
    This is the code for digraphs and graphs.
    The graphs implement the Adjacency list.

    The relevent Classes in this file are:
    - Node
    - Edge
    - Digraph
    - Graph
'''

class Node(object):
    def __init__(self, name):
        self.name = name;
    
    def getName(self):
        return self.name;
    
    def __str__(self):
        return self.name;


'''
    This object takes Nodes as source and destination.
'''
class Edge(object):
    def __init__(self, src_node, dest_node):
        self.src = src_node;
        self.dest = dest_node;
    
    def getSource(self):
        return self.src;
    
    def getDestination(self):
        return self.dest;
    
    def __str__(self):
        return "<" + self.src.getName() + ", " + self.dest.getName() + ">";

'''
    This is the implementation of a Directed Graph
'''
class Digraph(object):
    def __init__(self):
        self.edges = {};

    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Node already exist.");
        else:
            self.edges[node] = [];
    
    def addEdge(self, edge):
        src = edge.getSource();
        dest = edge.getDestination();
        if not (src in self.edges and dest in self.edges):
            raise ValueError("Node (source or destination) not in the graph");
        else:
            self.edges[src].append(dest);
    
    def childernOf(self, node):
        return self.edges[node];
    
    def hasNode(self, node):
        return node in self.edges;
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n;
        raise NameError(name);

    def __str__(self):
        result = "";
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + "->" + dest.getName() + "\n";
        return result;


'''
    This is the implementation of an undirected graph.
    It uses the fact that if we add the reverse of each
    edge in the directed graph we get an undirected graph
'''
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge);
        Digraph.addEdge(self, Edge(edge.getDestination(), edge.getSource())); 



###########################################################################################################
###################################### ********************************** #################################
###################################### SAMPLE IMPLEMENTATION OF THE GRAPH #################################
###################################### ********************************** #################################
###########################################################################################################


def buildGraph0(graphType):
    g = graphType();
    for name in (
        "Boston",
        "Providance",
        "New York",
        "Chicago",
        "Denver",
        "Phoenix",
        "Los Angeles"
    ):
        g.addNode(Node(name));
    
    g.addEdge(Edge(g.getNode("Boston"),     g.getNode("Providance")));
    g.addEdge(Edge(g.getNode("Boston"),     g.getNode("New York")));
    g.addEdge(Edge(g.getNode("Providance"), g.getNode("Boston")));
    g.addEdge(Edge(g.getNode("Providance"), g.getNode("New York")));
    g.addEdge(Edge(g.getNode("New York"),   g.getNode("Chicago")));
    g.addEdge(Edge(g.getNode("Chicago"),    g.getNode("Denver")));
    g.addEdge(Edge(g.getNode("Denver"),     g.getNode("Phoenix")));
    g.addEdge(Edge(g.getNode("Denver"),     g.getNode("New York")));
    g.addEdge(Edge(g.getNode("Chicago"),    g.getNode("Phoenix")));
    g.addEdge(Edge(g.getNode("Los Angeles"),g.getNode("Boston")));

    return g;


def buildGraph1(graphType):    
    nodes = []
    nodes.append(Node("ABC")) # nodes[0]
    nodes.append(Node("ACB")) # nodes[1]
    nodes.append(Node("BAC")) # nodes[2]
    nodes.append(Node("BCA")) # nodes[3]
    nodes.append(Node("CAB")) # nodes[4]
    nodes.append(Node("CBA")) # nodes[5]

    g = graphType()
    for n in nodes:
        g.addNode(n)
    return nodes,g;


def getAdjecentSwaped(string):
    yield string[1] + string[0] + string[2];
    yield string[0] + string[2] + string[1];

def main ():
    nodes, graph = buildGraph1(Digraph);
    for n in nodes:
        swaped = getAdjecentSwaped(n.getName());
        for s in swaped:
            for sn in nodes:
                if s == sn.getName():
                    graph.addEdge(Edge(graph.getNode(n.getName()), graph.getNode(sn.getName())));
    edges =  graph.childernOf(nodes[0]);
    for e in edges:
        print e.getName();

main();