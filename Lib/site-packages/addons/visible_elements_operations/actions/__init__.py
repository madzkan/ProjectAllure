"""This package contains all the addon proxy's actions."""
from .clearcontentsifvisibleandroid import ClearContentsIfVisibleAndroid
from .clearcontentsifvisibleios import ClearContentsIfVisibleiOS
from .clearcontentsifvisibleweb import ClearContentsIfVisibleWeb
from .clickifvisibleandroid import ClickIfVisibleAndroid
from .clickifvisibleios import ClickIfVisibleiOS
from .clickifvisibleweb import ClickIfVisibleWeb
from .containstextifvisibleandroid import ContainsTextIfVisibleAndroid
from .containstextifvisibleios import ContainsTextIfVisibleiOS
from .containstextifvisibleweb import ContainsTextIfVisibleWeb
from .gettextifvisibleandroid import GetTextIfVisibleAndroid
from .gettextifvisibleios import GetTextIfVisibleiOS
from .gettextifvisibleweb import GetTextIfVisibleWeb
from .isclickableandroid import IsClickableAndroid
from .isclickableios import IsClickableIOS
from .isclickableweb import IsClickableWeb
from .isselectedandroid import IsSelectedAndroid
from .isselectedios import IsSelectediOS
from .isselectedweb import IsSelectedWeb
from .longpressifvisibleandroid import LongPressIfVisibleAndroid
from .longpressifvisibleios import LongPressIfVisibleiOS
from .swipeandroid import SwipeAndroid
from .swipeios import SwipeIOS
from .tapifvisibleandroid import TapIfVisibleAndroid
from .tapifvisibleios import TapIfVisibleiOS
from .typetextifvisibleandroid import TypeTextIfVisibleAndroid
from .typetextifvisibleios import TypeTextIfVisibleiOS
from .typetextifvisibleweb import TypeTextIfVisibleWeb

__all__ = ["ClearContentsIfVisibleAndroid", "ClearContentsIfVisibleiOS", "ClearContentsIfVisibleWeb", "ClickIfVisibleAndroid", "ClickIfVisibleiOS", "ClickIfVisibleWeb", "ContainsTextIfVisibleAndroid", "ContainsTextIfVisibleiOS", "ContainsTextIfVisibleWeb", "GetTextIfVisibleAndroid", "GetTextIfVisibleiOS", "GetTextIfVisibleWeb",
           "IsClickableAndroid", "IsClickableIOS", "IsClickableWeb", "IsSelectedAndroid", "IsSelectediOS", "IsSelectedWeb", "LongPressIfVisibleAndroid", "LongPressIfVisibleiOS", "SwipeAndroid", "SwipeIOS", "TapIfVisibleAndroid", "TapIfVisibleiOS", "TypeTextIfVisibleAndroid", "TypeTextIfVisibleiOS", "TypeTextIfVisibleWeb"]
