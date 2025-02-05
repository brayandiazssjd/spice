from Beethoven.controller.controllers.Controller import Controller
from model.Wall import Wall


class WallController(Controller[Wall]):
    def __init__(self):
        super().__init__()
