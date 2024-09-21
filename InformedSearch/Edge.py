class Edge:
	"""docstring for ClassName"""
	def __init__(self, to: int, cost):
		self.to = to
		self.cost = cost

	def get_to(self):
		return self.to
	
	def get_cost(self):
		return self.cost