class edge:
    def __init__(self, node_head=None, node_tail=None, weight=0):
        self.__nodeHead = None
        self.__nodeTail = None
        self.__weight = 0

        if node_head is not None and node_tail is not None:
            self.connect(node_head, node_tail)
            self.setWeight(weight)

    def connect(self, node1, node2):
        self.__nodeHead = node1
        self.__nodeTail = node2
        self.__nodeHead.addEdge(self)
        self.__nodeTail.addEdge(self)

    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def getHead(self):
        return self.__nodeHead

    def getTail(self):
        return self.__nodeTail

    def getNeighbor(self, current_node):
        if current_node is self.__nodeHead:
            return self.__nodeTail
        if current_node is self.__nodeTail:
            return self.__nodeHead
        return None

    def links(self, node1, node2):
        return (
            (self.__nodeHead is node1 and self.__nodeTail is node2)
            or (self.__nodeHead is node2 and self.__nodeTail is node1)
        )


class node:
    def __init__(self, value):
        self.__value = value
        self.__connectedEdge = []

    def getValue(self):
        return self.__value

    def addEdge(self, connected_edge: edge):
        self.__connectedEdge.append(connected_edge)

    def getEdges(self):
        return self.__connectedEdge


class graph:
    def __init__(self):
        self.__startingNode = None

    def __resolve_node(self, target):
        if isinstance(target, node):
            return target
        return self.find(target)

    def __iter_nodes(self):
        if self.__startingNode is None:
            return

        visited = set()
        bfs_queue = [self.__startingNode]
        queue_index = 0

        while queue_index < len(bfs_queue):
            current = bfs_queue[queue_index]
            queue_index += 1

            if current in visited:
                continue

            visited.add(current)
            yield current

            for connected_edge in current.getEdges():
                neighbor = connected_edge.getNeighbor(current)
                if neighbor is not None and neighbor not in visited:
                    bfs_queue.append(neighbor)

    def __find_edge(self, node1, node2):
        for connected_edge in node1.getEdges():
            if connected_edge.links(node1, node2):
                return connected_edge
        return None

    def __iter_edges(self):
        seen_edges = set()

        for current_node in self.__iter_nodes() or []:
            for connected_edge in current_node.getEdges():
                edge_id = id(connected_edge)
                if edge_id in seen_edges:
                    continue
                seen_edges.add(edge_id)
                yield connected_edge

    def __connect_nodes(self, node1, node2, edge_weight=0):
        if node1 is node2:
            raise ValueError("cannot connect a node to itself")

        existing_edge = self.__find_edge(node1, node2)
        if existing_edge is not None:
            if edge_weight is not None:
                existing_edge.setWeight(edge_weight)
            return existing_edge

        new_edge = edge()
        new_edge.connect(node1, node2)
        new_edge.setWeight(edge_weight)
        return new_edge

    def addNodeByValue(self, value, connectNode=None, edgeWeight: int = 0):
        new_node = node(value)

        if self.__startingNode is None:
            self.__startingNode = new_node
            return new_node

        if connectNode is None:
            target_node = self.__startingNode
        else:
            target_node = self.__resolve_node(connectNode)
            if target_node is None:
                raise ValueError("connectNode not found in graph")

        self.__connect_nodes(target_node, new_node, edgeWeight)
        return new_node

    def addNodeByNode(self, new_node: node, connectNode=None, edgeWeight: int = 0):
        if not isinstance(new_node, node):
            raise TypeError("new_node must be an instance of node")

        if self.__startingNode is None:
            self.__startingNode = new_node
            return new_node

        if connectNode is None:
            target_node = self.__startingNode
        else:
            target_node = self.__resolve_node(connectNode)
            if target_node is None:
                raise ValueError("connectNode not found in graph")

        self.__connect_nodes(target_node, new_node, edgeWeight)
        return new_node

    def connectNodes(self, node1, node2, edgeWeight: int = 0):
        resolved_node1 = self.__resolve_node(node1)
        resolved_node2 = self.__resolve_node(node2)

        if resolved_node1 is None or resolved_node2 is None:
            raise ValueError("one or both nodes were not found in the graph")

        self.__connect_nodes(resolved_node1, resolved_node2, edgeWeight)

    def find(self, target):
        for current in self.__iter_nodes() or []:
            if isinstance(target, node):
                if current is target:
                    return current
            else:
                if current.getValue() == target:
                    return current
        return None

    def modifyEdgeWeight(self, node1, node2, newWeight: int):
        resolved_node1 = self.__resolve_node(node1)
        resolved_node2 = self.__resolve_node(node2)

        if resolved_node1 is None or resolved_node2 is None:
            raise ValueError("one or both nodes were not found in the graph")

        target_edge = self.__find_edge(resolved_node1, resolved_node2)
        if target_edge is None:
            raise ValueError("no edge found between the provided nodes")

        target_edge.setWeight(newWeight)

    def shortestPath(self, start, end):
        start_node = self.__resolve_node(start)
        end_node = self.__resolve_node(end)

        if start_node is None or end_node is None:
            raise ValueError("start or end node not found in graph")

        if start_node is end_node:
            return [start_node.getValue()], 0

        distances = {start_node: 0}
        previous = {}
        unvisited = list(self.__iter_nodes() or [])

        while unvisited:
            current_node = min(
                unvisited,
                key=lambda current: distances.get(current, float("inf")),
            )

            current_distance = distances.get(current_node, float("inf"))
            if current_distance == float("inf"):
                break

            unvisited.remove(current_node)

            if current_node is end_node:
                break

            for connected_edge in current_node.getEdges():
                neighbor = connected_edge.getNeighbor(current_node)
                if neighbor is None or neighbor not in unvisited:
                    continue

                candidate_distance = current_distance + connected_edge.getWeight()
                if candidate_distance < distances.get(neighbor, float("inf")):
                    distances[neighbor] = candidate_distance
                    previous[neighbor] = current_node

        if end_node not in distances:
            return [], float("inf")

        path_nodes = []
        traversal_node = end_node
        while traversal_node is not None:
            path_nodes.append(traversal_node.getValue())
            traversal_node = previous.get(traversal_node)

        path_nodes.reverse()
        return path_nodes, distances[end_node]

    def display(self):
        if self.__startingNode is None:
            print("Graph is empty")
            return "Graph is empty"

        lines = ["Graph:"]

        for current_node in self.__iter_nodes() or []:
            neighbors = []
            for connected_edge in current_node.getEdges():
                neighbor = connected_edge.getNeighbor(current_node)
                if neighbor is None:
                    continue
                neighbors.append(
                    f"{neighbor.getValue()}(w={connected_edge.getWeight()})"
                )

            if neighbors:
                lines.append(f"{current_node.getValue()} -> {', '.join(neighbors)}")
            else:
                lines.append(f"{current_node.getValue()} -> []")

        lines.append("Edges:")
        for connected_edge in self.__iter_edges():
            lines.append(
                f"{connected_edge.getHead().getValue()} --"
                f"({connected_edge.getWeight()})-- "
                f"{connected_edge.getTail().getValue()}"
            )

        output = "\n".join(lines)
        print(output)
        return output
