#!/usr/bin/env python


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: memsource_import_settings_info
short_description: Gather information about import settings available in Memsource.
version_added: 0.0.1
description:
    - Gather information about import settings available in Memsource
author: 'Yanis Guenane (@Spredzy)'
options:
  filters:
    description:
      - A dict of filters to apply.
      - Each dict item consists of a filter key and a filter value.
      - See U(https://cloud.memsource.com/web/docs/api#operation/getImportSettings) for possible filters.
    required: false
    default: {}
    type: dict
extends_documentation_fragment:
- community.memsource.memsource

requirements: [memsource]
"""

EXAMPLES = """
- name: Gather information about all available import settings
  community.memsource.memsource_import_settings_info:

- name: Gather information about a named import settings
  community.memsource.memsource_import_settings_info:
    filters:
      name: my-memsource-import-settings
"""

RETURN = """
import_settings:
    returned: on success
    description: >
        Memsource import settings that match the provided filters. Each element consists of a dict with all the information
        related to that import settings configuration.
    type: list
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.memsource.plugins.module_utils.memsource import (
    get_default_argspec,
    get_memsource_client,
)


def main():
    argument_spec = get_default_argspec()
    argument_spec = dict(filters=dict(default={}, type="dict"))

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    _memsource = get_memsource_client(module.params)

    import_settings = _memsource.get_import_settings(
        filters=module.params.get("filters")
    )

    module.exit_json(import_settings=import_settings)


if __name__ == "__main__":
    main()
