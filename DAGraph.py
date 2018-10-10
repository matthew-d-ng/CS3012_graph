
class DAGraph(object):

    def __init__(self):
        self.root = None
        self.nodes = dict()
        self.values = dict()

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return len(self.nodes)

    def contains(self, key):
        return key in self.nodes

    def addValue(self, key, value):
        if key is not None and value is not None:
            if self.isEmpty():
                self.root = key
            self.nodes[key] = []
            self.values[key] = value
            return True
        return False

    def getValue(self, key):
        if key is not None and self.contains(key):
            return self.values.getValue(key)
        return None

    def removeKey(self, key):
        if key in self.nodes:
            del self.values[key]
            del self.nodes[key]
            for node in self.nodes:
                i = node.find(key)
                if i >= 0:
                    node.remove(key)

    def addEdge(self, key1, key2):
        if key1 in self.nodes and key2 in self.nodes\
         and not self.pathTo(key2, key1):
            self.nodes[key1].append(key2)

    def pathTo(self, key1, key2):
        # TODO
        return False

    def getLowestCommonAncestor(self, key1, key2):
        # TODO
        return None

    def _getLowestCommonAncestor(self, currentNode, key1, key2):
        # TODO
        return currentNode.key
