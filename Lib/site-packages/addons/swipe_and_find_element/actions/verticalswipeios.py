"""This module contains the VerticalSwipeIOS proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class VerticalSwipeIOS(ActionProxy):
    def __init__(self, swipeDirection: str, bottomMarginPercent: int, topMarginPercent: int, maxSwipes: int, timeoutMilliseconds: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="3nqfr8Djt0KB-sz43jU-0g",
            classname="io.testproject.addons.mobile.elementfinder.Actions.iOS.VerticalSwipeIOS"
        )
        self.swipeDirection = swipeDirection
        self.bottomMarginPercent = bottomMarginPercent
        self.topMarginPercent = topMarginPercent
        self.maxSwipes = maxSwipes
        self.timeoutMilliseconds = timeoutMilliseconds
