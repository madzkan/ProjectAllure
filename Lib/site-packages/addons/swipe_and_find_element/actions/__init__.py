"""This package contains all the addon proxy's actions."""
from .horizontalswipeandroid import HorizontalSwipeAndroid
from .horizontalswipewithtextandroid import HorizontalSwipeWithTextAndroid
from .verticalswipeandroid import VerticalSwipeAndroid
from .horizontalswipeios import HorizontalSwipeIOS
from .horizontalswipewithtextios import HorizontalSwipeWithTextIOS
from .verticalswipeios import VerticalSwipeIOS
from .coordinateswipetoelement import CoordinateSwipeToElement
from .coordinateswipetoelement import CoordinateSwipeToElement
from .swipeuntilelementandroidhorizontal import SwipeUntilElementAndroidHorizontal
from .swipeuntilelementandroidvertical import SwipeUntilElementAndroidVertical
from .swipeuntilelementioshorizontal import SwipeUntilElementIOSHorizontal
from .swipeuntilelementiosvertical import SwipeUntilElementIOSVertical

__all__ = ["HorizontalSwipeAndroid", "HorizontalSwipeWithTextAndroid", "VerticalSwipeAndroid", "HorizontalSwipeIOS", "HorizontalSwipeWithTextIOS", "VerticalSwipeIOS", "CoordinateSwipeToElement",
           "CoordinateSwipeToElement", "SwipeUntilElementAndroidHorizontal", "SwipeUntilElementAndroidVertical", "SwipeUntilElementIOSHorizontal", "SwipeUntilElementIOSVertical"]
