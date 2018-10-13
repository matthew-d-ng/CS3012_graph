
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

    def getAllPaths(self, key1, key2, path=[]):
        """ returns a list of every path to key2 from key1 """
        if key1 in self.nodes and key2 in self.nodes:
            path = path + [key1]
            if key1 == key2:
                return [path]
            paths = []
            for key in self.nodes.get(key1):
                if key not in path:
                    newpaths = self.getAllPaths(key, key2, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            return paths
        return None

    def getLowestCommonAncestor(self, key1, key2):
        """ Returns a list of all lowest common ancestors for 2 keys
            Returns None for no common ancestors found
            (Brute Force) """
        # Uses a lot of memory B)
        if key1 in self.nodes and key2 in self.nodes:
            # Get 2 dicts of ancestors (key:depth)
            key1ancestors = self._getAncestors(key1)
            key2ancestors = self._getAncestors(key2)
            if key1ancestors is None or key2ancestors is None:
                return None
            # Finding common ancestors
            common = dict()
            for key, depth in key1ancestors.items():
                if key in key2ancestors:
                    common[key] = depth
            if len(common) == 0:
                return None
            # find lowest common ancestors i.e largest depth
            # a DAG can have multiple LCAs for a pair of nodes
            lowestCommon = list()
            lowest = None
            for key, depth in common.items():
                if lowest is None or depth > lowest:
                    lowest = depth
            for key, depth in common.items():
                if depth == lowest:
                    lowestCommon.append(key)
            return lowestCommon
        return None

    def _getAncestors(self, key):
        paths = self.getAllPaths(self.root, key)
        if len(paths) == 0:
            return None
        ancestors = dict()
        for path in paths:
            for depth in range(len(path)):
                if path[depth] not in ancestors\
                        or depth < ancestors[path[depth]]:
                    ancestors[path[depth]] = depth
        return ancestors
