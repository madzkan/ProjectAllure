"""This module contains the ClearContentsIfVisibleAndroid proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ClearContentsIfVisibleAndroid(ActionProxy):
    def __init__(self, timeout: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="inW2AJJ04ku45E9-RN2zqA",
            classname="io.testproject.addon.ClearContentsActions.ClearContentsIfVisibleAndroid"
        )
        self.timeout = timeout
