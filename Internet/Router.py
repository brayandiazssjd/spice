import random
from Packet import Packet

class Router:
	def __init__(self, id, ping) -> None:
		self.__id = id
		self.__ping = ping

	# The method to call when sending the data
	def send(self, destiny_id, packet):
		pass

	# the method to actually trasfer the packet and follow the router (hop_list)
	def transfer(self, hop_list, packet):
		pass

	# Return a list with the route from the router to the destiny
	def __trace_route(self, destiny_id):
		pass
		#return route

	# Returns the weighted value of the edge between the nodes (current router and destiny)
	def weight(self, destiny_id):
		return (self.ping() + self.bsearch(destiny_id).ping()) / 2

	@property
	def table(self):
		return self.__table

	@table.setter
	def table(self, value):
		self.__table = value

	@property
	def ping(self):
		return self.__ping + self.__delay()

	@table.setter
	def table(self, value):
		self.__ping = value

	def __delay(self):
		return random.random()

	# Binary seach in the hop table
	def bsearch(self, id):
		pass
