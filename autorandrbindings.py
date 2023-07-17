#!/bin/python
from subprocess import run
from typing import List


def __available_profiles__() -> List[str]:
    return run(
        ["autorandr", "--list"], encoding="utf-8", capture_output=True
    ).stdout.splitlines()


def available_profiles() -> List[str]:
    return sorted(__available_profiles__())


def set_profile(profile: str) -> None:
    if profile in __available_profiles__():
        run(["autorandr", profile])
    else:
        raise ValueError("Profile {} is not a registered profile".format(profile))


def current_profile() -> str:
    return __available_profiles__()[0]
