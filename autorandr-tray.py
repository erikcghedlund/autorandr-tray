#!/bin/python
from os import path, getcwd
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import autorandrbindings as autorandr

__location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))


def set_state(s: str):
    def inner(icon, item):
        autorandr.set_profile(s)

    return inner


def get_state(s: str):
    def inner(item):
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
