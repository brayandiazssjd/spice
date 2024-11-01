import random
from Packet import Packet

class Router:

	def __init__(self, id, name, ping, variance) -> None:
		self.__id = id
		self.__ping = ping # ping en nanosegundos
		self.__name = name
		self.__variance = variance
		self.__buffer = []


	# Simulates http protocol
	def http(self, destiny_id, packets, route):
		random.shuffle(packets)
		for packet in packets:
			packet.route = route
			self.send(packet)
			if random.random() > 0.89:
				print("Paquete perdidido. Reenviando...")
			print("Paquete: ", packet.id, "Ruta: ", packet.route)

	# the method to actually trasfer the packet and follow the router (hop_list)
	def send(self, packet: Packet):

		if packet.destiny == self.__id:
			self.__buffer.append(packet)
			return
		next_r = self.__search(packet.next_ip())
		if not next_r:
			print("Error")
		else:
			next_r.send(packet)

	# Returns the weighted value of the edge between the nodes (current router and destiny)
	def weight(self, destiny_id):
		return int((self.ping() + self.__search(destiny_id).ping()) / 2)

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
		return next((p for p in self.__table if p.id == ip), None)
		
	def show_message(self):
		mss = ""
		self.__buffer.sort(key = lambda x: x.id)
		for p in self.__buffer:
			mss += p.playload
		print(self.__name, ":", mss)
		self.__buffer = []