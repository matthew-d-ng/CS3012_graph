import BinaryGraph
import unittest

class graphTest(unittest.TestCase):


    def __init__(self):
        self.graph = BinaryGraph()
        
    def testForEmptyGraph(self):
    
        assert self.graph.isEmpty() == True, "empty graph returned as empty", "empty graph returning non-empty"
        assert self.graph.size() == 0, "size of empty graph is 0", "size of empty graph not 0"
        assert self.graph.contains('A') == False, "empty graph does not contain key A", "empty graph contains key A"
        assert self.graph.getValue('A') == None, "Empty graph correctly return nothing for key A", \
                                                "Empty graph returning values for non existent node"
        assert self.graph.addValue('A', 1), "return true for succesfully added node to empty graph", "node won't add to empty graph"

    def testForNonEmptyGraph(self):
    
        assert self.graph.getValue('A') == 1, "return correct value for key A after adding to empty graph",\
                                            "value not returned after adding to empty graph"
         # TODO: finish tests                                       