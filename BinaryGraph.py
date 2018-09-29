
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
        if currentNode is None:
            return self.GraphNode(key, value)
        elif currentNode.key < key:
            currentNode.left = self._addValue(currentNode.left, key, value)
        elif currentNode.key > key:
            currentNode.right = self._addValue(currentNode.right, key, value)
        currentNode.size = 1 + self._getSize(currentNode.left) \
                             + self._getSize(currentNode.right)
        return currentNode

    def getValue(self, key):
        if key is not None and self.root is not None:
            return self._getValue(self.root, key)
        else:
            return None

    def _getValue(self, currentNode, key):
        if currentNode is not None:
            if currentNode.key == key:
                return currentNode.value
            elif currentNode.key > key:
                return self._getValue(currentNode.right, key)
            else:
                return self._getValue(currentNode.left, key)
        else:
            return None

    def removeKey(self, key):
        self.root = self._removeKey(self.root, key)

    def _removeKey(self, currentNode, key):
        if currentNode is None:
            return None
        if currentNode.key < key:
            currentNode.left = self._removeKey(currentNode.left, key)
        elif currentNode.key > key:
            currentNode.right = self._removeKey(currentNode.right, key)
        else:
            if currentNode.right is None:
                return currentNode.left
            if currentNode.left is None:
                return currentNode.right

            pred = self._findPred(currentNode, currentNode.key)
            self._removePred(currentNode)
            pred.left = currentNode.left
            pred.right = currentNode.right
            currentNode = pred

        currentNode.size = self._getSize(currentNode.left) \
            + self._getSize(currentNode.right) + 1
        return currentNode

    def _findPred(self, currentNode, key):
        if currentNode.key == key:
            return self._findPred(currentNode.left, key)
        if currentNode.right is not None:
            return self._findPred(currentNode.right, key)
        return currentNode

    def _removePred(self, currentNode):
        pred = self._findPred(currentNode, currentNode.key)
        return self._removeKey(self.root, pred.key)
