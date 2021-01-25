#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os

from memsource import Memsource


def get_action(module_params):
    """Get action to do based on module.params"""

    trimmed_list = {
        k: v
        for k, v in module_params.items()
        if v is not None and k not in get_default_argspec().keys() and k != "state"
    }

    if module_params.get("state") == "absent":
        action = "delete"
    elif not module_params.get("uid"):
        action = "create"
    elif list(trimmed_list.keys()) == ["uid"]:
        action = "read"
    else:
        action = "update"

    return action


def get_memsource_client(module_params):
    """Return a memsource client instance"""

    if os.environ.get("MEMSOURCE_TOKEN"):
        # TO BE IMPLEMENTED in python-memsource
        memsource_client = None
    elif module_params.get("memsource_token"):
        # TO BE IMPLEMENTED in python-memsource
        memsource_client = None
    elif os.environ.get("MEMSOURCE_USERNAME") and os.environ.get("MEMSOURCE_PASSWORD"):
        memsource_client = Memsource(
            os.environ.get("MEMSOURCE_USERNAME"), os.environ.get("MEMSOURCE_PASSWORD")
        )
    elif module_params.get("memsource_username") and module_params.get(
        "memsource_password"
    ):
        memsource_client = Memsource(
            module_params.get("memsource_username"),
            module_params.get("memsource_password"),
        )
    else:
        memsource_client = None

    return memsource_client


def get_default_argspec():
    """
    Provides default argument spec for the options documented in the memsource doc fragment.
    """

    return dict(
        memsource_username=dict(type="str"),
        memsource_password=dict(type="str", no_log=True),
        memsource_token=dict(type="str", no_log=True),
    )
