
class BinaryGraph(object):

    def __init__(self):
        self.size = 0
        self.head = None

    class GraphNode(object):

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def contains(self, key):
        return self.getValue(key) is not None

    def addValue(self, key, value):
        if not self.contains(key):
            return None  # TODO

    def getValue(self, key):
        if key is not None and self.head is not None:
            return self._getValue(self.head, key)
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
