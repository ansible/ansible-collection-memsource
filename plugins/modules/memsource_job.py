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
  uid:
    description:
      - UID of the job
    type: str
  project_uid:
    description:
      - UID of the project the job's belong to
    type: str
  source_lang:
    description:
      - Source language of the job
    type: str
  target_langs:
    description:
      - Target languages for the job
    type: list
extends_documentation_fragment:
- community.memsource.memsource

requirements: [memsource]
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
    filename: /path/to/file

- name: Retrieve job information
  community.memsource.memsource_job:
    uid: uid
    project_uid: project_uid

- name: Delete job
  community.memsource.memsource_job:
    uid: uid
    projectu_id: project_uid
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
            project_uid=dict(type="str"),
            langs=dict(type="list"),
            filename=dict(type="path"),
            use_project_file_import_settings=dict(type="bool"),
            purge_on_delete=dict(type="bool"),
            split_filename_on_dir=dict(type="bool"),
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
                "use_project_file_import_settings", True
            )
        }
        job = _memsource.create_job(
            module.params.get("project_uid"),
            module.params.get("langs"),
            module.params.get("filename"),
            module.params.get("split_filename_on_dir", False),
            **kwargs
        )
        _result.update({"changed": True})
    elif _action == "read":
        job = _memsource.get_job_by_id(
            module.params["uid"], module.params["project_uid"]
        )
    elif _action == "update":
        pass
    else:
        res = _memsource.delete_job(
            module.params["uid"],
            module.params["project_uid"],
            purge=module.params.get("purge_on_delete", False),
            do_not_fail_on_404=True,
        )
        if res.status_code == 204:
            _result.update({"changed": True})

    _result.update({"job": job})

    module.exit_json(**_result)


if __name__ == "__main__":
    main()
