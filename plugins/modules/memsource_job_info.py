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
  project:
    description:
      - Name of the project to retrieved jobs for.
      - This option is mutually exclusive with C(project_id).
  project_id:
    description:
      - ID of the project to retrieved jobs for
      - This option is mutually exclusive with C(project).
  filters:
    description:
      - A dict of filters to apply.
      - Each dict item consists of a filter key and a filter value.
      - See U(https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) for possible filters.
      - Filter names and values are case sensitive.
      - You can use underscores instead of dashes (-) in the filter keys.
      - Filter keys with underscores will take precedence in case of conflict.
    required: false
    default: {}
    type: dict
extends_documentation_fragment:
- community.memsource.memsource

requirements: [python-memsource]
"""

EXAMPLES = """
- name: Gather information about all available templates
  community.memsource.memsource_job_info:
    project: Project101

- name: Gather information about a specific job
  community.memsource.memsource_job:
    project: Project101
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
        project=dict(type="str"),
        project_id=dict(type="int"),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[["project", "project_id"]],
        mutually_exclusive=[["project", "project_id"]],
    )

    _memsource = get_memsource_client(module.params)

    if module.params.get("project"):
        project_id = _memsource.get_projects(
            filters={"name": module.params["project"]}
        )[0]["id"]
    else:
        project_id = module.params.get("project_id")

    jobs = _memsource.get_jobs(project_id, filters=module.params.get("filters"))

    module.exit_json(jobs=jobs)


if __name__ == "__main__":
    main()
