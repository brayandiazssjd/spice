from model.Activity import Activity
from .Controller import Controller


class ActivityController(Controller[Activity]):
    def __init__(self):
        super().__init__()
