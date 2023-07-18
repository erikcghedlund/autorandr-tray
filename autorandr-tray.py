#!/bin/python
from os import path, getcwd
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import autorandrbindings as autorandr

__location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))


def set_state(s: str):
    """Set the state of a profile.

    Args:
        s: The state to set the profile to

    Returns:
        A function that sets the profile state
    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """
    def inner(icon, item):
        """Sets the profile for autorandr.

        Args:
            icon: The icon to set.
            item: The item to set.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        autorandr.set_profile(s)

    return inner


def get_state(s: str):
    """Get a function that checks if the current state matches the given state.

    Args:
        s: The state to check against

    Returns:
        A function that takes an item and returns True if the current state matches the given state, False otherwise.
    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """
    def inner(item):
        """Check if the current profile is equal to the given item.

        Args:
            item: The item to compare with the current profile.

        Returns:
            True if the current profile is equal to the item, False otherwise.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        return autorandr.current_profile() == s

    return inner


# Let the menu items be a callable returning a sequence of menu
# items to allow the menu to grow
icon(
    "test",
    Image.open(path.join(__location__, "icon.png")),
    menu=menu(
        lambda: (
            item(profile, set_state(profile), checked=get_state(profile), radio=True)
            for profile in autorandr.available_profiles()
        )
    ),
).run()
