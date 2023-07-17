#!/bin/python
from subprocess import run


def __available_profiles__():
    return run(
        ["autorandr", "--list"], encoding="utf-8", capture_output=True
    ).stdout.splitlines()


def available_profiles():
    return sorted(__available_profiles__())


def set_profile(profile: str):
    if profile in __available_profiles__():
        run(["autorandr", profile])
    else:
        raise ValueError("Profile {} is not a registered profile".format(profile))


def current_profile():
    return __available_profiles__()[0]
