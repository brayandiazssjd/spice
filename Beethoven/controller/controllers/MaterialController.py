from Beethoven.controller.controllers.Controller import Controller
from Beethoven.model.Material import Material


class MaterialController(Controller[Material]):
    def __init__(self):
        super().__init__()
