from.Factory import Factory
from model.Activity import Activity
from typing import Dict


class ActivityFactory(Factory[Activity]):
    def __init__(self) -> None:
        super().__init__()

    def create(self, data: Dict) -> Activity:
        activity = Activity()
        activity.id = data['id']
        activity.local_noise = data['local_noise']
        activity.name = data['name']
        activity.start = data['start']
        activity.end = data['end']
        activity.external_noise = data['external_noise'] 
        return activity
