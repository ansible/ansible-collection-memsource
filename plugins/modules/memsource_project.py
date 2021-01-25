#!/usr/bin/env python


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: memsource_project
short_description: Manage a Memsource project
version_added: 0.0.1
description:
    - Manage a Memsource project
author: 'Yanis Guenane (@Spredzy)'
options:
  uid:
    description:
      - UID of the project
    type: str
  name:
    description:
      - A dict of filters to apply
    required: false
    default: {}
    type: dict
  template_id:
    description:
      - A dict of filters to apply
    required: false
    default: {}
    type: dict
  purge_on_delete:
    description:
      - Whether to purge the content of the project on delete
    type: bool
extends_documentation_fragment:
- community.memsource.memsource

requirements: [memsource]
"""

EXAMPLES = """
- name: Create project from template id
  community.memsource.memsource_project:
    name: My Project
    template_id: 12345

- name: Retrieve project information
  community.memsource.memsource_project:
    uid: uid

- name: Delete project
  community.memsource.memsource_project:
    uid: uid
    state: absent
"""

RETURN = """
project:
    returned: on success
    description: >
        Project's up to date information
    type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.memsource.plugins.module_utils.memsource import (
    get_action,
    get_default_argspec,
    get_memsource_client,
)


def main():
    argument_spec = get_default_argspec()
    argument_spec.update(
        dict(
            uid=dict(type="str"),
            name=dict(type="str"),
            template_id=dict(type="int"),
            purge_on_delete=dict(type="bool"),
            state=dict(type="str", default="present", choices=["absent", "present"]),
        ),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    _memsource = get_memsource_client(module.params)
    _action = get_action(module.params)
    _result = {}
    project = {}

    if _action == "create":
        if module.params.get("template_id"):
            project = _memsource.create_project_from_template(
                module.params.get("name"), module.params.get("template_id")
            )
        else:
            pass
        _result.update({"changed": True})
    elif _action == "read":
        project = _memsource.get_project_by_id(module.params["uid"])
    elif _action == "update":
        pass
    else:
        res = _memsource.delete_project(
            module.params["uid"],
            purge=module.params.get("purge_on_delete", False),
            do_not_fail_on_404=True,
        )
        if res.status_code == 204:
            _result.update({"changed": True})

    _result.update({"project": project})

    module.exit_json(**_result)


if __name__ == "__main__":
    main()
