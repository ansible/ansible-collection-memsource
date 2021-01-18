#!/usr/bin/env python


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: memsource_job
short_description: Manage a Memsource job
version_added: 0.0.1
description:
    - Manage a Memsource job
author: 'Yanis Guenane (@Spredzy)'
options:
  name:
    description:
      - A dict of filters to apply.
    required: false
    default: {}
    type: dict
  template:
    description:
      - A dict of filters to apply.
    required: false
    default: {}
    type: dict
  template_id:
    description:
      - A dict of filters to apply.
    required: false
    default: {}
    type: dict
  source_lang:
    description:
      - A dict of filters to apply.
    required: false
    default: {}
    type: dict
  target_langs:
    description:
      - A dict of filters to apply.
    required: false
    default: {}
    type: dict
extends_documentation_fragment:
- community.memsource.memsource

requirements: [python-memsource]
"""

EXAMPLES = """
# Project creation
#
- name: Create job
  community.memsource.memsource_job:
    name: My Project
    source_lang: en_us
    target_langs:
      - ja_jp
      - zh_cn

- name: Retrieve job information
  community.memsource.memsource_job:
    uid: uid
    project_id: project_id

- name: Delete job
  community.memsource.memsource_job:
    uid: uid
    project_id: project_id
    state: absent
"""

RETURN = """
job:
    returned: on success
    description: >
        Job's up to date information
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
            project_id=dict(type="int"),
            langs=dict(type="list"),
            filename=dict(type="path"),
            use_project_file_import_settings=dict(type="bool"),
            purge_on_delete=dict(type="bool"),
            state=dict(type="str", default="present", choices=["absent", "present"]),
        ),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    _memsource = get_memsource_client(module.params)
    _action = get_action(module.params)
    _result = {}
    job = {}

    if _action == "create":
        kwargs = {
            "useProjectFileImportSettings": module.params.get(
                "use_project_file_import_settings", False
            )
        }
        job = _memsource.create_job(
            module.params.get("project_id"),
            module.params.get("langs"),
            module.params.get("filename"),
            **kwargs
        )
        _result.update({"changed": True})
    elif _action == "read":
        job = _memsource.get_job_by_id(
            module.params["uid"], module.params["project_id"]
        )
    elif _action == "update":
        pass
    else:
        res = _memsource.delete_job(
            module.params["uid"],
            module.params["project_id"],
            purge=module.params.get("purge_on_delete", False),
            do_not_fail_on_404=True,
        )
        if res.status_code == 204:
            _result.update({"changed": True})

    _result.update({"job": job})

    module.exit_json(**_result)


if __name__ == "__main__":
    main()
