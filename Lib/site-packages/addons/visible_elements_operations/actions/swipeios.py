"""This module contains the SwipeIOS proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class SwipeIOS(ActionProxy):
    def __init__(self, direction: str, swipeDistance: int = 50, swipeDuration: int = 1000):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="inW2AJJ04ku45E9-RN2zqA",
            classname="io.testproject.addon.SwipeActions.SwipeIOS"
        )
        self.direction = direction
        self.swipeDistance = swipeDistance
        self.swipeDuration = swipeDuration
