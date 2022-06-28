#!/usr/bin/env python


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: memsource_project_info
short_description: Get the recent project from Memsource on passing the project name parameter.
version_added: 0.0.1
description:
    - Get the recent project from Memsource on passing the project name parameter
author: 'Yanis Guenane (@Spredzy)'
options:
  project_name:
    description:
      - A string passed as the project name which matches the project name on Memsource
    required: true
    type: str
extends_documentation_fragment:
- ansible.memsource.memsource

requirements: [memsource]
"""

EXAMPLES = """
- name: Get Project by Project Name
  ansible.memsource.memsource_project_info:
    project_name: "{{ project_name }}"
  register: _project

- name: Set Project UID from project name {{ _project }}
  set_fact: 
    project_uid: "{{ _project.projects.content[0].uid }}"
"""

RETURN = """
project:
    returned: on success
    description: >
        Returns the json response for the specified project name
    type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ansible.memsource.plugins.module_utils.memsource import (
    get_default_argspec,
    get_memsource_client,
)


def main():
    argument_spec = get_default_argspec()
    argument_spec.update(dict(project_name=dict(type="str", required=True)))

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    _memsource = get_memsource_client(module.params)

    project = _memsource.get_project_by_name(module.params.get("project_name"))

    module.exit_json(projects=project)


if __name__ == "__main__":
    main()
