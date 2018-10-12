from DAGraph import DAGraph
import unittest


class GraphTest(unittest.TestCase):

    def __init__(self):
        self.graph = DAGraph()

    def testForEmptyGraph(self):

        assert self.graph.isEmpty(), "empty graph returning non-empty"

        assert self.graph.getSize() == 0, "size of empty graph not 0"

        assert not self.graph.contains(5), "empty graph contains key 5"

        assert self.graph.getValue(5) is None,\
            "Empty graph returning values for non existent node"

        assert self.graph.addValue(5, 'a'),\
            "node won't add to empty graph"

    def testForNonEmptyGraph(self):

        assert self.graph.getValue(5) == 'a',\
            "value not returned after adding to empty graph"

        self.graph.addValue(1, 'b')
        self.graph.removeKey(1)
        assert self.graph.getValue(1) is None, "key 1 didn't remove"
        assert self.graph.getPathFromRoot(1) is None,\
            "returning non-existent path from 5 to 1"

        self.graph.addValue(1, 'b')
        self.graph.addValue(8, 'c')
        assert self.graph.addEdge(5, 1), "edge failed to add"
        self.graph.addEdge(1, 8)
        assert self.graph.getPathFromRoot(8) == [5, 1, 8],\
            "path to 8 unexpected path"
        assert not self.graph.addEdge(8, 5), "cycle created in acyclic graph"

        # build a graph
        self.graph.addValue(4, 'd')
        self.graph.addEdge(1, 4)
        self.graph.addEdge(8, 4)
        self.graph.addValue(6, 'e')
        self.graph.addEdge(4, 6)
        self.graph.addEdge(8, 6)
        self.graph.addValue(7, 'f')
        self.graph.addEdge(6, 7)

        assert self.graph.getPathFromRoot(4) == [5, 1, 4], \
            "no path to key 4 found"
        assert self.graph.getPathFromRoot(7) == [5, 1, 8, 6, 7] or\
            self.graph.getPathFromRoot(7) == [5, 1, 4, 6, 7],\
            "no path to key 7 found"

    def testLCA(self):

        self.graph.addValue(11, 'g')
        self.graph.addValue(10, 'h')
        self.graph.addValue(12, 'i')

        self.graph.addEdge(7, 10)
        self.graph.addEdge(7, 11)
        self.graph.addEdge(11, 12)

        # ancestor checking goes through one of the nodes
        assert self.graph.getLowestCommonAncestor(10, 7) == 7,\
            "LCA failed, expected key 7 on keys 10 and 7"

        # ancestor should be directly above the two nodes
        assert self.graph.getLowestCommonAncestor(11, 10) == 7,\
            "LCA failed, expected key 7 on keys 11 and 10"

        # checking for keys further away
        assert self.graph.getLowestCommonAncestor(12, 10) == 7,\
            "LCA failed for distant ancestor 7 for keys 12 and 10"

        # key doesn't exist
        assert self.graph.getLowestCommonAncestor(13, 4) is None,\
            "didn't return none for non-existent key for some reason"


# main
tests = GraphTest()
tests.testForEmptyGraph()
tests.testForNonEmptyGraph()
# tests.testLCA()
print("Concluded tests.")
