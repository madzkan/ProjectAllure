"""This module contains the VerticalSwipeAndroid proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class VerticalSwipeAndroid(ActionProxy):
    def __init__(self, swipeDirection: str, bottomMarginPercent: int, topMarginPercent: int, maxSwipes: int, timeoutMilliseconds: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="3nqfr8Djt0KB-sz43jU-0g",
            classname="io.testproject.addons.mobile.elementfinder.Actions.Android.VerticalSwipeAndroid"
        )
        self.swipeDirection = swipeDirection
        self.bottomMarginPercent = bottomMarginPercent
        self.topMarginPercent = topMarginPercent
        self.maxSwipes = maxSwipes
        self.timeoutMilliseconds = timeoutMilliseconds
