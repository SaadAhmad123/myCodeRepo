def printPath(path):
    pathString = "";
    for nodes in path:
        pathString += str(nodes) + "->";
    pathString = pathString[0:len(pathString)-2];
    print pathString;

def dfs(graph, start, end, path, shortest, toPrint):
    path = path + [start];
    if toPrint:
        printPath(path);
    if start == end:
        return path;
    for node in graph.childernOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = dfs(graph, node, end, path, shortest, toPrint);
                if newPath != None:
                    shortest = newPath;
        elif toPrint:
            print ("Already visited ", str(node))
    return shortest;

def getShortestPath(graph, start, end, toPrint = False):
    return dfs(graph, graph.getNode(start), graph.getNode(end), [], None, toPrint);
