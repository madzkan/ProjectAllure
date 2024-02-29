"""This module contains the ContainsTextIfVisibleWeb proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ContainsTextIfVisibleWeb(ActionProxy):
    def __init__(self, text: str, timeout: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="inW2AJJ04ku45E9-RN2zqA",
            classname="io.testproject.addon.ContainsTextActions.ContainsTextIfVisibleWeb"
        )
        self.text = text
        self.timeout = timeout
