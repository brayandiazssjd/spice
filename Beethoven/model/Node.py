from typing import Optional, Tuple, List
from model.Room import Room


class Node:

    def __init__(self, id: int, room: Optional[Room], color = None):
        self.id = id
        self.room = room
        self.color: Optional[int] = color
        self.edges: Optional[List[Tuple[int, float]]] = []  # Lista de conexiones con otros nodos

    def add_edge(self, nbr: int, weight: float):
        self.edges.append((nbr, weight))  # Conexión con habitación y la pared que los une

    def __str__(self):
        return f"(id={self.id}, room={str(self.room)}, color={self.color}, edges={self.edges})"
