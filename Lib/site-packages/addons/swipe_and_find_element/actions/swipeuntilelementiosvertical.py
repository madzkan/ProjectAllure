"""This module contains the SwipeUntilElementIOSVertical proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class SwipeUntilElementIOSVertical(ActionProxy):
    def __init__(self, direction: str, amountOfSwipes: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="3nqfr8Djt0KB-sz43jU-0g",
            classname="io.testproject.addons.mobile.elementfinder.SimpleSwipes.SimpleIOS.SwipeUntilElementIOSVertical"
        )
        self.direction = direction
        self.amountOfSwipes = amountOfSwipes
