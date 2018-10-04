
class BinaryGraph(object):

    def __init__(self):
        self.root = None

    class GraphNode(object):

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.size = 1

    def getSize(self):
        return self._getSize(self.root)

    def _getSize(self, node):
        if node is not None:
            return node.size
        return 0

    def isEmpty(self):
        return self.getSize() == 0

    def contains(self, key):
        return self.getValue(key) is not None

    def addValue(self, key, value):
        if key is not None and value is not None:
            self.root = self._addValue(self.root, key, value)
            return True
        return False

    def _addValue(self, currentNode, key, value):
        # TODO
        return currentNode

    def getValue(self, key):
        if key is not None and self.root is not None:
            return self._getValue(self.root, key)
        else:
            return None

    def _getValue(self, currentNode, key):
        # TODO
        return None

    def removeKey(self, key):
        self.root = self._removeKey(self.root, key)

    def _removeKey(self, currentNode, key):
        # TODO
        return currentNode

    def getLowestCommonAncestor(self, key1, key2):
        if key1 is not None and key2 is not None and self.root is not None:
            if self.contains(key1) and self.contains(key2):
                if key1 != key2:
                    return self._getLowestCommonAncestor(self.root, key1, key2)
                else:
                    return key1
        return None

    def _getLowestCommonAncestor(self, currentNode, key1, key2):
        if key1 < currentNode.key and key2 < currentNode.key:
            return self._getLowestCommonAncestor(currentNode.left, key1, key2)
        if key1 > currentNode.key and key2 > currentNode.key:
            return self._getLowestCommonAncestor(currentNode.right, key1, key2)
        return currentNode.key
