"""This module contains the SwipeUntilElementAndroidHorizontal proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class SwipeUntilElementAndroidHorizontal(ActionProxy):
    def __init__(self, direction: str, amountOfSwipes: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="3nqfr8Djt0KB-sz43jU-0g",
            classname="io.testproject.addons.mobile.elementfinder.SimpleSwipes.SimpleAndroid.SwipeUntilElementAndroidHorizontal"
        )
        self.direction = direction
        self.amountOfSwipes = amountOfSwipes
