"""This module contains the GetTextIfVisibleWeb proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetTextIfVisibleWeb(ActionProxy):
    def __init__(self, timeout: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="inW2AJJ04ku45E9-RN2zqA",
            classname="io.testproject.addon.GetTextActions.GetTextIfVisibleWeb"
        )
        self.text = None
        self.timeout = timeout
