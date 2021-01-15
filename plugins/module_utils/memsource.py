#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os

from memsource import Memsource


def get_memsource_client(module_params):
    """Return a memsource client instance"""

    if os.environ.get("MEMSOURCE_TOKEN"):
        # TO BE IMPLEMENTED in python-memsource
        pass
    elif module_params.get("memsource_token"):
        # TO BE IMPLEMENTED in python-memsource
        pass
    elif os.environ.get("MEMSOURCE_USERNAME") and os.environ.get("MEMSOURCE_PASSWORD"):
        return Memsource(
            os.environ.get("MEMSOURCE_USERNAME"), os.environ.get("MEMSOURCE_PASSWORD")
        )
    elif module_params.get("memsource_username") and module_params.get(
        "memsource_password"
    ):
        return Memsource(
            module_params.get("memsource_username"),
            module_params.get("memsource_password"),
        )
    else:
        return None


def get_default_argspec():
    """
    Provides default argument spec for the options documented in the memsource doc fragment.
    """

    return dict(
        memsource_user=dict(type="str"),
        memsource_password=dict(type="str", no_log=True),
        memsource_token=dict(type="str", no_log=True),
    )
