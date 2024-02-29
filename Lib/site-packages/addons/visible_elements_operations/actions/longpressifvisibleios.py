"""This module contains the LongPressIfVisibleiOS proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class LongPressIfVisibleiOS(ActionProxy):
    def __init__(self, duration: str, timeout: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="inW2AJJ04ku45E9-RN2zqA",
            classname="io.testproject.addon.LongPressActions.LongPressIfVisibleiOS"
        )
        self.duration = duration
        self.timeout = timeout
