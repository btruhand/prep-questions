from python.graphs.adjacency_graph import AdjacencyGraph
from functools import reduce
from typing import Dict, Sequence, List
import unittest

def mesh_message(network: Dict[str, Sequence[str]], fromNode: str, toNode: str) -> List[str]:
	"""Mesh message
	Finding the shortest path given from one network to another network

	:param network: The given known network
	:type network: Dict[str, Sequence[str]]
	:param fromNode: Where the message is coming from
	:type fromNode: str
	:param toNode: Where the message is going to
	:type toNode: str
	:return: A list of network nodes
	:rtype: List[str]

	.. seealso::

	   The problem was given from `mesh-message
	   https://www.interviewcake.com/question/python/mesh-message`_
	"""
	graph = AdjacencyGraph()
	for node, neighbours in network.items():
		graph.addVertex(node)
		reduce(lambda acc, neighbour: graph.addVertex(neighbour).addEdge(node, neighbour), neighbours, graph)

	return graph.shortestPath(fromNode, toNode)

class TestMeshMessage(unittest.TestCase):
	def test_sample_input(self):
		  network = {\
			'Min'     : ['William', 'Jayden', 'Omar'],
			'William' : ['Min', 'Noam'],
			'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
			'Ren'     : ['Jayden', 'Omar'],
			'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
			'Adam'    : ['Amelia', 'Miguel'],
			'Miguel'  : ['Amelia', 'Adam'],
			'Noam'    : ['Nathan', 'Jayden', 'William'],
			'Omar'    : ['Ren', 'Min']
		  }

		  self.assertEqual(['Omar', 'Ren'], mesh_message(network, 'Omar', 'Ren'))
		  self.assertEqual(['Min', 'Jayden', 'Amelia', 'Adam'], mesh_message(network, 'Min', 'Adam'))

unittest.main()