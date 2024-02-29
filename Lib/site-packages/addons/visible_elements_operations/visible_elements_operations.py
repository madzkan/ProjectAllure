from .actions import ClearContentsIfVisibleAndroid, ClearContentsIfVisibleiOS, ClearContentsIfVisibleWeb, ClickIfVisibleAndroid, ClickIfVisibleiOS, ClickIfVisibleWeb, ContainsTextIfVisibleAndroid, ContainsTextIfVisibleiOS, ContainsTextIfVisibleWeb, GetTextIfVisibleAndroid, GetTextIfVisibleiOS, GetTextIfVisibleWeb, IsClickableAndroid, IsClickableIOS, IsClickableWeb, IsSelectedAndroid, IsSelectediOS, IsSelectedWeb, LongPressIfVisibleAndroid, LongPressIfVisibleiOS, SwipeAndroid, SwipeIOS, TapIfVisibleAndroid, TapIfVisibleiOS, TypeTextIfVisibleAndroid, TypeTextIfVisibleiOS, TypeTextIfVisibleWeb


class VisibleElementsOperations:
    @staticmethod
    def clearcontentsifvisibleandroid(timeout: str) -> ClearContentsIfVisibleAndroid:
        """Clear the contents of {{element}} if it's visible."""
        return ClearContentsIfVisibleAndroid(timeout)

    @staticmethod
    def clearcontentsifvisibleios(timeout: str) -> ClearContentsIfVisibleiOS:
        """Clear the contents of {{element}} if it's visible."""
        return ClearContentsIfVisibleiOS(timeout)

    @staticmethod
    def clearcontentsifvisibleweb(timeout: str) -> ClearContentsIfVisibleWeb:
        """Clear the contents of {{element}} if it's visible."""
        return ClearContentsIfVisibleWeb(timeout)

    @staticmethod
    def clickifvisibleandroid(timeout: str) -> ClickIfVisibleAndroid:
        """Click {{element}} if it's visible."""
        return ClickIfVisibleAndroid(timeout)

    @staticmethod
    def clickifvisibleios(timeout: str) -> ClickIfVisibleiOS:
        """Click {{element}} if it's visible."""
        return ClickIfVisibleiOS(timeout)

    @staticmethod
    def clickifvisibleweb(timeout: str) -> ClickIfVisibleWeb:
        """Click {{element}} if it's visible."""
        return ClickIfVisibleWeb(timeout)

    @staticmethod
    def containstextifvisibleandroid(text: str, timeout: str) -> ContainsTextIfVisibleAndroid:
        """{{element}} contains text {{text}}?."""
        return ContainsTextIfVisibleAndroid(text, timeout)

    @staticmethod
    def containstextifvisibleios(text: str, timeout: str) -> ContainsTextIfVisibleiOS:
        """{{element}} contains text {{text}}?."""
        return ContainsTextIfVisibleiOS(text, timeout)

    @staticmethod
    def containstextifvisibleweb(text: str, timeout: str) -> ContainsTextIfVisibleWeb:
        """{{element}} contains text {{text}}?."""
        return ContainsTextIfVisibleWeb(text, timeout)

    @staticmethod
    def gettextifvisibleandroid(timeout: str) -> GetTextIfVisibleAndroid:
        """Get text from {{element}} if it's visible."""
        return GetTextIfVisibleAndroid(timeout)

    @staticmethod
    def gettextifvisibleios(timeout: str) -> GetTextIfVisibleiOS:
        """Get text from {{element}} if it's visible."""
        return GetTextIfVisibleiOS(timeout)

    @staticmethod
    def gettextifvisibleweb(timeout: str) -> GetTextIfVisibleWeb:
        """Get text from {{element}} if it's visible."""
        return GetTextIfVisibleWeb(timeout)

    @staticmethod
    def isclickableandroid(timeout: str) -> IsClickableAndroid:
        """Is {{element}} clickable?."""
        return IsClickableAndroid(timeout)

    @staticmethod
    def isclickableios(timeout: str) -> IsClickableIOS:
        """Is {{element}} clickable?."""
        return IsClickableIOS(timeout)

    @staticmethod
    def isclickableweb(timeout: str) -> IsClickableWeb:
        """Is {{element}} clickable?."""
        return IsClickableWeb(timeout)

    @staticmethod
    def isselectedandroid(timeout: str) -> IsSelectedAndroid:
        """Is {{element}} selected?."""
        return IsSelectedAndroid(timeout)

    @staticmethod
    def isselectedios(timeout: str) -> IsSelectediOS:
        """Is {{element}} selected?."""
        return IsSelectediOS(timeout)

    @staticmethod
    def isselectedweb(timeout: str) -> IsSelectedWeb:
        """Is {{element}} selected?."""
        return IsSelectedWeb(timeout)

    @staticmethod
    def longpressifvisibleandroid(duration: str, timeout: str) -> LongPressIfVisibleAndroid:
        """Make a long press gesture on {{element}} if it's visible."""
        return LongPressIfVisibleAndroid(duration, timeout)

    @staticmethod
    def longpressifvisibleios(duration: str, timeout: str) -> LongPressIfVisibleiOS:
        """Make a long press gesture on {{element}} if it's visible."""
        return LongPressIfVisibleiOS(duration, timeout)

    @staticmethod
    def swipeandroid(direction: str, swipeDistance: int, swipeDuration: int) -> SwipeAndroid:
        """Swipes ON an android element if he is visible.

        Swipes in a given direction on an Android Element if he is visible.
        """
        return SwipeAndroid(direction, swipeDistance, swipeDuration)

    @staticmethod
    def swipeios(direction: str, swipeDistance: int, swipeDuration: int) -> SwipeIOS:
        """Swipes ON an IOS element if he is visible.

        Swipes in a given direction on an IOS Element if he is visible.
        """
        return SwipeIOS(direction, swipeDistance, swipeDuration)

    @staticmethod
    def tapifvisibleandroid(timeout: str) -> TapIfVisibleAndroid:
        """Tap {{element}} if it's visible."""
        return TapIfVisibleAndroid(timeout)

    @staticmethod
    def tapifvisibleios(timeout: str) -> TapIfVisibleiOS:
        """Tap {{element}} if it's visible."""
        return TapIfVisibleiOS(timeout)

    @staticmethod
    def typetextifvisibleandroid(text: str, timeout: str) -> TypeTextIfVisibleAndroid:
        """Type {{text}} in {{element}} if visible."""
        return TypeTextIfVisibleAndroid(text, timeout)

    @staticmethod
    def typetextifvisibleios(text: str, timeout: str) -> TypeTextIfVisibleiOS:
        """Type {{text}} in {{element}} if visible."""
        return TypeTextIfVisibleiOS(text, timeout)

    @staticmethod
    def typetextifvisibleweb(text: str, timeout: str) -> TypeTextIfVisibleWeb:
        """Type {{text}} in {{element}} if visible."""
        return TypeTextIfVisibleWeb(text, timeout)
