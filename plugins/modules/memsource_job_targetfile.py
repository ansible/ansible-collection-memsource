#!/usr/bin/env python


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: memsource_job_targetfile
short_description: Download a Memsource target file
version_added: 0.0.1
description:
    - Download a Memsource target file
author: 'Yanis Guenane (@Spredzy)'
options:
  project_uid:
    description:
      - UID of the project the job belongs to
    required: true
    type: str
  job_uid:
    description:
      - UID of the job the target file is attached to
    required: true
    type: str
  path:
    description:
      - Path where to install the downloaded file. If not specified
        it will rely on filename and original directory provided by
        the Memsource API
    required: false
    type: path
  force:
    description:
      - Whether to force write the downloaded file
    required: false
    type: bool
extends_documentation_fragment:
- community.memsource.memsource

requirements: [memsource]
"""

EXAMPLES = """
- name: Download job target file and rely on filename and original directory name for dest
  community.memsource.memsource_job_file:
    project_uid: xxx
    jobs_uid: yyy

- name: Download job target file and write it in path
  community.memsource.memsource_job_file:
    project_uid: xxx
    jobs_uid: yyy
    path: /tmp/foo
"""

RETURN = """
job_file:
    returned: on success
    description: >
        TBD
    type: dict
"""

import os.path

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
            project_uid=dict(type="str", required=True),
            job_uid=dict(type="str", required=True),
            path=dict(type="path"),
            force=dict(type="bool"),
        ),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    _memsource = get_memsource_client(module.params)
    _result = {}

    res = _memsource.get_job_targetfile(
        module.params.get("job_uid"), module.params.get("project_uid")
    )

    job = _memsource.get_job_by_id(
        module.params.get("job_uid"), module.params.get("project_uid")
    )

    if module.params.get("path") is not None:
        _dest = module.params.get("path")
    else:
        _dest = "%s%s" % (job["originalFileDirectory"], job["filename"])

    if os.path.exists(_dest) and not module.params.get("force", False):
        pass
    else:
        content = "%s\n" % str(res.content.decode("utf-8")).split("\n\r\n")[1]
        with open(_dest, "w+") as ftw:
            ftw.write(content)
        _result.update({"changed": True})

    module.exit_json(**_result)


if __name__ == "__main__":
    main()
