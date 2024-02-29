"""This module contains the LongPressIfVisibleAndroid proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class LongPressIfVisibleAndroid(ActionProxy):
    def __init__(self, duration: str, timeout: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="inW2AJJ04ku45E9-RN2zqA",
            classname="io.testproject.addon.LongPressActions.LongPressIfVisibleAndroid"
        )
        self.duration = duration
        self.timeout = timeout
