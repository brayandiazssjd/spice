import random
from Packet import Packet

class Router:

	def __init__(self, id, name, ping, variance) -> None:
		self.__id = id
		self.__ping = ping # ping en nanosegundos
		self.__name = name
		self.__variance = variance
		self.__buffer = ""

	# Simulates http protocol
	def http(self, destiny_id, packets):
		for packet in packets:
			packet.route = self.__trace_route(destiny_id)
			self.send(packet)

	# the method to actually trasfer the packet and follow the router (hop_list)
	def send(self, packet: Packet):
		next_ip = self.__search(packet.next_ip())
		if packet.destiny == self.__id:
			self.__buffer += packet.playload
			return
		self.__search(packet.next_ip()).send(packet)

	def error(self, packet: Packet):
		route = packet.route
		route = route[:packet.next_hop - 1]
		route = route.reverse()
		# Crea un packet de error y lo envía de vuelta

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

	@property
	def id(self):
		return self.__id

	# Return a true with probability of p
	def __rand_reach(self, p):
		if random.random() > p:
			return False
		return True

	# Binary seach in the hop table
	def __search(self, ip):
		return next((p for p in self.__table if p.ip == ip), None)
		
	def show_message(self):
		print(self.__buffer)
		self.__buffer = ""