from BinaryGraph import BinaryGraph
import unittest


class GraphTest(unittest.TestCase):

    def __init__(self):
        self.graph = BinaryGraph()

    def testForEmptyGraph(self):

        assert self.graph.isEmpty(), ("empty graph returned as empty",
                                      "empty graph returning non-empty")

        assert self.graph.getSize() == 0, ("size of empty graph is 0",
                                           "size of empty graph not 0")

        assert not self.graph.contains(5),\
            ("empty graph does not contain key 5",
             "empty graph contains key 5")

        assert self.graph.getValue(5) is None,\
            ("Empty graph correctly return nothing for key B",
             "Empty graph returning values for non existent node")

        assert self.graph.addValue(5, 1),\
            ("return true for succesfully added node to empty graph",
             "node won't add to empty graph")

    def testForNonEmptyGraph(self):

        assert self.graph.addValue(1, 1)
        self.graph.removeKey(1)
        assert self.graph.getValue(1) is None,\
            ("removed key 1 is None",
             "key 1 didn't remove")

        assert self.graph.addValue(8, 1)
        self.graph.removeKey(8)
        assert self.graph.getValue(8) is None,\
            ("removed key 8 is None",
             "key 8 didn't remove")

        assert self.graph.getValue(5) == 1,\
            ("return correct value for key 5 after adding to empty graph",
             "value not returned after adding to empty graph")

        self.graph.addValue(4, 9)
        self.graph.addValue(6, 7)
        self.graph.addValue(7, 10)

        assert self.graph.getValue(4) == 9,\
            ("value of key 4 correctly added to existing graph",
             "value of key 4 not added to existing graph")
        assert self.graph.getValue(7) == 10,\
            ("value of key 7 correctly added to existing graph",
             "value of key 7 not added to existing graph")

        def testLCA(self):

            self.graph.addValue(11, 12)
            self.graph.addValue(10, 13)
            self.graph.addValue(12, 14)

            # ancestor checking goes through one of the nodes
            assert self.graph.getLowestCommonAncestor(10, 11) == 7,\
                ("correctly received close ancestor key 7 for 12 and 11"
                 "LCA failed, expected key 7 on keys 12 and 11")

            # ancestor should be directly above the two nodes
            assert self.graph.getLowestCommonAncestor(12, 10) == 11,\
                ("correctly received close ancestor key 11 for 12 and 10"
                 "LCA failed, expected key 11 on keys 12 and 10")

            # checking for keys further away
            assert self.graph.getLowestCommonAncestor(12, 4) == 5,\
                ("correctly found distant ancestor key 5 for 12 and 4",
                 "LCA failed for distant ancestor 5 for keys 12 and 4")

            # key doesn't exist
            assert self.graph.getLowestCommonAncestor(13, 4) is None,\
                ("correctly found None for value that doesn't exist",
                 "didn't return none for non-existent key for some reason")


# main
tests = GraphTest()
tests.testForEmptyGraph()
tests.testForNonEmptyGraph()
print("Concluded tests.")
