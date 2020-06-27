class Node:
    def __init__(self, data=None, directed: bool = False):
        self.data = data
        self.neighbors = []
        self.directed = directed

    def addNeighbor(self, newNeighbor: "Node") -> None:
        if not self.hasNeighbor(newNeighbor):
            self.neighbors.append(newNeighbor)
            if not self.directed:
                newNeighbor.addNeighbor(self)

    def _addNeighbor(self, newNeighbors: list("Node")) -> None:
        for newNeighbor in newNeighbors:
            self.addNeighbor(newNeighbor)

    def hasNeighbor(self, neighbor: "Node") -> bool:
        return neighbor in self.neighbors

    def __str__(self):
        rv = "{}".format(self.data)
        for n in self.neighbors:
            rv += "->" + str(n.data)
        return rv


def main():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    # G = Node(7)
    # H = Node(8)
    # I = Node(9)
    # J = Node(10)

    A._addNeighbor([B, C, D])
    B._addNeighbor([C])
    C._addNeighbor([F])
    F._addNeighbor([C])

    print(A)
    print(B)
    print(C)
    print(D)
    print(E)
    print(F)


main()
