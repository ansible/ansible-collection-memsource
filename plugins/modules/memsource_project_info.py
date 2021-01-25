#!/usr/bin/env python


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: memsource_project_info
short_description: Gather information about projects available in Memsource.
version_added: 0.0.1
description:
    - Gather information about projects available in Memsource
author: 'Yanis Guenane (@Spredzy)'
options:
  filters:
    description:
      - A dict of filters to apply.
      - Each dict item consists of a filter key and a filter value.
      - See U(https://cloud.memsource.com/web/docs/api#operation/getProject) for possible filters.
    required: false
    default: {}
    type: dict
extends_documentation_fragment:
- community.memsource.memsource

requirements: [memsource]
"""

EXAMPLES = """
- name: Gather information about all available projects
  community.memsource.memsource_project_info:

- name: Gather information about a named project
  community.memsource.memsource_project_info:
    filters:
      name: my-memsource-template
"""

RETURN = """
projects:
    returned: on success
    description: >
        Memsource templates that match the provided filters. Each element consists of a dict with all the information
        related to that template.
    type: list
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.memsource.plugins.module_utils.memsource import (
    get_default_argspec,
    get_memsource_client,
)


def main():
    argument_spec = get_default_argspec()
    argument_spec.update(dict(filters=dict(default={}, type="dict")))

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    _memsource = get_memsource_client(module.params)

    projects = _memsource.get_projects(filters=module.params.get("filters"))

    module.exit_json(projects=projects)


if __name__ == "__main__":
    main()
