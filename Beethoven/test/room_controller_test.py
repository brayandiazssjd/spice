from controller.controllers.RoomController import RoomController

rc: RoomController = RoomController()
rc.create_test_rooms()
g = rc.get_graph()

print([str(g.nodes[i]) for i in range(3)])

