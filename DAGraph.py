
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
            return self.values.get(key)
        return None

    def removeKey(self, key):
        if key in self.nodes:
            del self.values[key]
            del self.nodes[key]
            for node, adjacents in self.nodes.items():
                if key in adjacents:
                    node.remove(key)

    def addEdge(self, key1, key2):
        if key1 in self.nodes and key2 in self.nodes\
         and not self.pathTo(key2, key1):
            self.nodes[key1].append(key2)
            return True
        return False

    def pathTo(self, key1, key2):
        return self.getPath(key1, key2) is not None

    def getPathFromRoot(self, key):
        return self.getPath(self.root, key)

    def getPath(self, key1, key2, path=[]):
        """ Returns the shortest path to a node """
        if key1 in self.nodes and key2 in self.nodes:
            path = path + [key1]
            if key1 == key2:
                return path
            short = None
            for key in self.nodes.get(key1):
                if key not in path:
                    newPath = self.getPath(key, key2, path)
                    if newPath:
                        if not short or len(newPath) < len(short):
                            short = newPath
            return short
        return None

    def getLowestCommonAncestor(self, key1, key2):
        # TODO
        # get all paths from to both nodes from root
        return None
