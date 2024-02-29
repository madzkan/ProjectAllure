"""This module contains the ContainsTextIfVisibleiOS proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ContainsTextIfVisibleiOS(ActionProxy):
    def __init__(self, text: str, timeout: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="inW2AJJ04ku45E9-RN2zqA",
            classname="io.testproject.addon.ContainsTextActions.ContainsTextIfVisibleiOS"
        )
        self.text = text
        self.timeout = timeout
