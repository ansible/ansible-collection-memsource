#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r"""
options:
  memsource_token:
    description:
      - The OAuth token to use to connect to cloud.memsource.com.
    type: str
  memsource_username:
    description:
      - The username to use for BasicAuth to connect to cloud.memsource.com.
    type: str
  memsource_password:
    description:
      - The password to use for BasicAuth to connect to cloud.memsource.com.
    type: str
requirements:
  - python-memsource
notes:
  - If parameters are not set within the module, the following
    environment variables can be used.
    C(MEMSOURCE_TOKEN), or C(MEMSOURCE_USERNAME) and C(MEMSOURCE_PASSWORD)
  - If both Token based and BasicAuth parameters are specified, the Token
    based mechanism will have precedence.
"""
