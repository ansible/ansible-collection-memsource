#!/usr/bin/env python


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: memsource_job_info
short_description: Gather information about jobs for a specific project in Memsource.
version_added: 0.0.1
description:
    - Gather information about jobs for a specific project in Memsource
author: 'Yanis Guenane (@Spredzy)'
options:
  project_uid:
    description:
      - UID of the project to retrieved jobs for
      - This option is mutually exclusive with C(project).
  filters:
    description:
      - A dict of filters to apply.
      - Each dict item consists of a filter key and a filter value.
      - See U(https://cloud.memsource.com/web/docs/api#operation/getPart) for possible filters.
    required: false
    default: {}
    type: dict
extends_documentation_fragment:
- community.memsource.memsource

requirements: [memsource]
"""

EXAMPLES = """
- name: Gather information about a specific job
  community.memsource.memsource_job:
    project_uid: 123456
    filters:
      targetLang: ja_jp
"""

RETURN = """
jobs:
    returned: on success
    description: >
        Memsource jobs that match the provided filters and project. Each element consists of a dict with all the information
        related to those jobs.
    type: list
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.memsource.plugins.module_utils.memsource import (
    get_default_argspec,
    get_memsource_client,
)


def main():
    argument_spec = get_default_argspec()
    argument_spec = dict(
        filters=dict(default={}, type="dict"),
        project_uid=dict(type="str", required=True),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    _memsource = get_memsource_client(module.params)

    jobs = _memsource.get_jobs(
        module.params.get("project_uid"), filters=module.params.get("filters")
    )

    module.exit_json(jobs=jobs)


if __name__ == "__main__":
    main()
