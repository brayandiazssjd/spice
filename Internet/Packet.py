class Packet:
	def __init__(self, playload):
		self.__ttl = 8
		self.__next_hop = 0
		self.__playload = playload
		self.__route = []
		self.time = 0

	# Returns the next hop
	def next_ip(self):
		if self.__next_hop < len(self.__route):
			next_ip = self.__route[self.__next_hop]
			self.__next_hop += 1
			return next_ip
		return None

	@property
	def route(self):
		return self.__route

	@route.setter
	def route(self, value):
		self.__route = value

	@property
	def ttl(self):
		self.__ttl -= 1
		return self.__ttl
	
	@property
	def origin(self):
		return self.__route[0]

	@origin.setter
	def origin(self, value):
		self.__route.insert(0, value)

	@property
	def destiny(self):
		return self.__route[len(self.__route)]

	@destiny.setter
	def destiny(self, value):
		self.__route.append(value)