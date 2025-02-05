from controller.controllers.Controller import Controller
from model.Material import Material


class MaterialController(Controller[Material]):
    def __init__(self):
        super().__init__()
