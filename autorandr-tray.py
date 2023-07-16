#!/bin/python
from os import path, getcwd
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import autorandrbindings as autorandr

__location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))


def create_image():
    # Generate an image and draw a pattern
    return Image.open(path.join(__location__, "icon.png"))


def set_state(v):
    def inner(icon, item):
        autorandr.set_profile(v)

    return inner


def get_state(v):
    def inner(item):
        return autorandr.current_profile() == v

    return inner


# Let the menu items be a callable returning a sequence of menu
# items to allow the menu to grow
icon(
    "test",
    create_image(),
    menu=menu(
        lambda: (
            item(profile, set_state(profile), checked=get_state(profile), radio=True)
            for profile in autorandr.available_profiles()
        )
    ),
).run()
