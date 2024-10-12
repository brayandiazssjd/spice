import random
from Packet import Packet

class Router:

	def __init__(self, id, name, ping, variance) -> None:
		self.__id = id
		self.__ping = ping
		self.__name = name
		self.__variance = variance

	# The method to call when sending the data
	def send(self, destiny_id, packet):
		packet.route = self.__trace_route(destiny_id)
		self.transfer(packet)

	# the method to actually trasfer the packet and follow the router (hop_list)
	def transfer(self, packet):
		next = self.__search(packet.next())
		if packet.destiny == self.__id:
		  print()
		# if self.__rand_reach(0.90):
		# 	next.transfer(hop_list[1:], packet)
		pass

	# Return a list with the routers ip from the router to the destiny
	def __trace_route(self, destiny_id):
		pass
		#return route

	# Returns the weighted value of the edge between the nodes (current router and destiny)
	def weight(self, destiny_id):
		return (self.ping() + self.__search(destiny_id).ping()) / 2

	@property
	def table(self):
		return self.__table

	@table.setter
	def table(self, value):
		self.__table = value

	# Returns it's ping plus a random variance.
	@property
	def ping(self):
		return self.__ping + random.randint(-self.__variance, self.__variance)

	@property
	def name(self):
		return self.__name

	# Return a true with probability of p
	def __rand_reach(self, p):
		if random.random() > p:
			return False
		return True

	# Binary seach in the hop table
	def __search(self, ip):
		return next((p for p in self.__table if p.ip == ip), None)
		
