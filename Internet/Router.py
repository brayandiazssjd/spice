import random
from Packet import Packet

class Router:
	def __init__(self, id, name, ping) -> None:
		self.__id = id
		self.__ping = ping
		self.__name = name

	# The method to call when sending the data
	def send(self, destiny_id, packet):
		# self.transfer(calculate route, packet)
		pass

	# the method to actually trasfer the packet and follow the router (hop_list)
	def transfer(self, hop_list, packet):
		# next = self.search(hop_list[:1])
		# if not next:
		#   error packet
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

	@property
	def ping(self):
		return self.__ping + self.__delay()

	@property
	def name(self):
		return self.__name
	

	def __delay(self):
		return random.random()

	# Return a true with probability of p
	def __rand_reach(self, p):
		if random.random() > p:
			return False
		return True

	# Binary seach in the hop table
	def __search(self, ip):
		return next((p for p in self.__table if p.ip == ip), None)
		
