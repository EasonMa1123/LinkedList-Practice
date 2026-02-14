class edge:
    def __init__(self):
        self.__nodeHead = None
        self.__nodeTail = None
        self.__weight = 0
    
    def connect(self,node1,node2):
        self.__nodeHead = node1
        self.__nodeTail = node2
        self.__nodeHead.addEdge(self)
        self.__nodeTail.addEdge(self)

    def setWeight(self,weight):
        self.__weight = weight
    
class node:
    def __init__(self,value):
        self.__value = value
        self.__connectedEdge = []

    def getValue(self):
        return self.__value
    
    def addEdge(self,edge:edge):
        self.__connectedEdge.append(edge)
import queue
class graph:
    
    def __init__(self):
        self.__startingNode = None

    def addNodeByValue(self, value, connectNode=None, edgeWeight: int = 0):
        new_node = node(value)

        # If graph is empty
        if self.__startingNode is None:
            self.__startingNode = new_node
            return new_node

        # Determine connection target
        if connectNode is None:
            target_node = self.__startingNode
        else:
            target_node = self.find(connectNode)
            if target_node is None:
                raise ValueError("connectNode value not found in graph")

        # Create and connect edge
        new_edge = edge()
        new_edge.connect(target_node, new_node)

        if edgeWeight != 0:
            new_edge.setWeight(edgeWeight)

        return new_node


    def addNodeByNode(self, new_node: node, connectNode=None, edgeWeight: int = 0):

        # If graph is empty
        if self.__startingNode is None:
            self.__startingNode = new_node
            return new_node

        # Determine which node to connect to
        if connectNode is None:
            connectNode = self.__startingNode

        # Create edge and connect
        new_edge = edge()
        new_edge.connect(connectNode, new_node)

        if edgeWeight != 0:
            new_edge.setWeight(edgeWeight)

        return new_node

    def find(self, target):
        if self.__startingNode is None:
            return None

        visited = set()
        q = queue(100)  # adjust size as needed
        q.append(self.__startingNode)

        while not q.isEmpty():
            current = q.dequeue()

            if current in visited:
                continue

            visited.add(current)

            # Case 1: searching by node object
            if isinstance(target, node):
                if current is target:
                    return current

            # Case 2: searching by value
            else:
                if current.getValue() == target:
                    return current

            # Traverse edges
            for e in current._node__connectedEdge:
                if e._edge__nodeHead is current:
                    neighbor = e._edge__nodeTail
                else:
                    neighbor = e._edge__nodeHead

                if neighbor not in visited:
                    q.append(neighbor)

        return None
