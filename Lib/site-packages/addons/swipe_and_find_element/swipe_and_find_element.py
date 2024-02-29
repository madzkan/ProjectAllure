from .actions import HorizontalSwipeAndroid, HorizontalSwipeWithTextAndroid, VerticalSwipeAndroid, HorizontalSwipeIOS, HorizontalSwipeWithTextIOS, VerticalSwipeIOS, CoordinateSwipeToElement, CoordinateSwipeToElement, SwipeUntilElementAndroidHorizontal, SwipeUntilElementAndroidVertical, SwipeUntilElementIOSHorizontal, SwipeUntilElementIOSVertical


class SwipeAndFindElement:
    @staticmethod
    def horizontalswipeandroid(swipeDirection: str, rightMarginPercent: int, leftMarginPercent: int, maxSwipes: int, timeoutMilliseconds: int) -> HorizontalSwipeAndroid:
        """Swipe {{element}} {{swipeDirection}} searching for {{locator}}={{locatorValue}}."""
        return HorizontalSwipeAndroid(swipeDirection, rightMarginPercent, leftMarginPercent, maxSwipes, timeoutMilliseconds)

    @staticmethod
    def horizontalswipewithtextandroid(text: str, swipeDirection: str, rightMarginPercent: int, leftMarginPercent: int, maxSwipes: int, timeoutMilliseconds: int) -> HorizontalSwipeWithTextAndroid:
        """Swipe {{element}} {{swipeDirection}} searching for sub-element with text {{text}}."""
        return HorizontalSwipeWithTextAndroid(text, swipeDirection, rightMarginPercent, leftMarginPercent, maxSwipes, timeoutMilliseconds)

    @staticmethod
    def verticalswipeandroid(swipeDirection: str, bottomMarginPercent: int, topMarginPercent: int, maxSwipes: int, timeoutMilliseconds: int) -> VerticalSwipeAndroid:
        """Swipe {{swipeDirection}} to {{element}}."""
        return VerticalSwipeAndroid(swipeDirection, bottomMarginPercent, topMarginPercent, maxSwipes, timeoutMilliseconds)

    @staticmethod
    def horizontalswipeios(swipeDirection: str, rightMarginPercent: int, leftMarginPercent: int, maxSwipes: int, timeoutMilliseconds: int) -> HorizontalSwipeIOS:
        """Swipe {{element}} {{swipeDirection}} searching for {{locator}}={{locatorValue}}."""
        return HorizontalSwipeIOS(swipeDirection, rightMarginPercent, leftMarginPercent, maxSwipes, timeoutMilliseconds)

    @staticmethod
    def horizontalswipewithtextios(text: str, swipeDirection: str, rightMarginPercent: int, leftMarginPercent: int, maxSwipes: int, timeoutMilliseconds: int) -> HorizontalSwipeWithTextIOS:
        """Swipe {{element}} {{swipeDirection}} searching for sub-element with text {{text}}."""
        return HorizontalSwipeWithTextIOS(text, swipeDirection, rightMarginPercent, leftMarginPercent, maxSwipes, timeoutMilliseconds)

    @staticmethod
    def verticalswipeios(swipeDirection: str, bottomMarginPercent: int, topMarginPercent: int, maxSwipes: int, timeoutMilliseconds: int) -> VerticalSwipeIOS:
        """Swipe {{swipeDirection}} to {{element}}."""
        return VerticalSwipeIOS(swipeDirection, bottomMarginPercent, topMarginPercent, maxSwipes, timeoutMilliseconds)

    @staticmethod
    def coordinateswipetoelement(startXMargin: int, startYMargin: int, endXMargin: int, endYMargin: int, amountOfSwipes: int) -> CoordinateSwipeToElement:
        """Swipe Between Specified Point Margins Until Element Displayed.

        Swipe between coordinates until element is displayed.
        """
        return CoordinateSwipeToElement(startXMargin, startYMargin, endXMargin, endYMargin, amountOfSwipes)

    @staticmethod
    def coordinateswipetoelement(startXMargin: int, startYMargin: int, endXMargin: int, endYMargin: int, amountOfSwipes: int) -> CoordinateSwipeToElement:
        """Swipe Between Specified Point Margins Until Element Displayed.

        Swipe between coordinates until element is displayed.
        """
        return CoordinateSwipeToElement(startXMargin, startYMargin, endXMargin, endYMargin, amountOfSwipes)

    @staticmethod
    def swipeuntilelementandroidhorizontal(direction: str, amountOfSwipes: int) -> SwipeUntilElementAndroidHorizontal:
        """Swipe {{direction}} at Most {{amountOfSwipes}} Times Until Element is Displayed.

        Swipes in given direction until element is displayed.
        """
        return SwipeUntilElementAndroidHorizontal(direction, amountOfSwipes)

    @staticmethod
    def swipeuntilelementandroidvertical(direction: str, amountOfSwipes: int) -> SwipeUntilElementAndroidVertical:
        """Swipe {{direction}} at Most {{amountOfSwipes}} Times Until Element is Displayed.

        Swipes in given direction until element is displayed.
        """
        return SwipeUntilElementAndroidVertical(direction, amountOfSwipes)

    @staticmethod
    def swipeuntilelementioshorizontal(direction: str, amountOfSwipes: int) -> SwipeUntilElementIOSHorizontal:
        """Swipe {{direction}} at Most {{amountOfSwipes}} Times Until Element is Displayed.

        Swipes in given direction until element is displayed.
        """
        return SwipeUntilElementIOSHorizontal(direction, amountOfSwipes)

    @staticmethod
    def swipeuntilelementiosvertical(direction: str, amountOfSwipes: int) -> SwipeUntilElementIOSVertical:
        """Swipe {{direction}} at Most {{amountOfSwipes}} Times Until Element is Displayed.

        Swipes in given direction until element is displayed.
        """
        return SwipeUntilElementIOSVertical(direction, amountOfSwipes)
