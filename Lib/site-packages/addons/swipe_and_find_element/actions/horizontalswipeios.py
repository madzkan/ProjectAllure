"""This module contains the HorizontalSwipeIOS proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class HorizontalSwipeIOS(ActionProxy):
    def __init__(self, swipeDirection: str, rightMarginPercent: int, leftMarginPercent: int, maxSwipes: int, timeoutMilliseconds: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="3nqfr8Djt0KB-sz43jU-0g",
            classname="io.testproject.addons.mobile.elementfinder.Actions.iOS.HorizontalSwipeIOS"
        )
        self.swipeDirection = swipeDirection
        self.rightMarginPercent = rightMarginPercent
        self.leftMarginPercent = leftMarginPercent
        self.maxSwipes = maxSwipes
        self.timeoutMilliseconds = timeoutMilliseconds
