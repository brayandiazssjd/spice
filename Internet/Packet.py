class Packet:
	def __init__(self, connection, id, length, playload):
		self.__next_hop = 1
		self.playload = playload
		self.route = []
		self.time = 0
		self.id = id
		self.connection_id = connection
		self.lenght = length

	# Returns the next hop
	def next_ip(self):
		if self.__next_hop < len(self.route):
			next_ip = self.route[self.__next_hop]
			self.__next_hop += 1
			return next_ip
		return None
	
	@property
	def origin(self):
		return self.route[0]

	@origin.setter
	def origin(self, value):
		self.route.insert(0, value)

	@property
	def destiny(self):
		return self.route[len(self.route)-1]

	@destiny.setter
	def destiny(self, value):
		self.route.append(value)

	@property
	def next_hop(self):
		return self.__next_hop