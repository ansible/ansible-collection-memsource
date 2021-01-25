#!/usr/bin/env python


from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: memsource_import_settings
short_description: Manage a Memsource import settings configuration
version_added: 0.0.1
description:
    - Manage a Memsource import settings configuration
author: 'Yanis Guenane (@Spredzy)'
options:
  input_charset:
    description:
      - TODO
    type: str
  output_charset:
    description:
      - TODO
    type: str
  zip_charset:
    description:
      - TODO
    type: str
  file_Format:
    description:
      - TODO
    type: str
  file_format_configuration:
    description:
      - TODO
    type: dict
  target_length:
    description:
      - TODO
    type: bool
  target_length_max:
    description:
      - TODO
    type: str
  target_length_percent:
    description:
      - TODO
    type: bool
  target_length_percent_value:
    description:
      - TODO
    type: int
  segmentation_rule_id:
    description:
      - TODO
    type: int
  target_segmentation_rule_id:
    description:
      - TODO
    type: int
extends_documentation_fragment:
- community.memsource.memsource

requirements: [memsource]
"""

EXAMPLES = """
"""

RETURN = """
import_settings:
    returned: on success
    description: >
        Import Settings' up to date information
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
            output_charset=dict(type="str"),
            zip_charset=dict(type="str"),
            file_format=dict(type="str"),
            file_format_configuration=dict(type="dict"),
            target_length=dict(type="bool"),
            target_length_max=dict(type="str"),
            target_length_percent=dict(type="bool"),
            target_length_perence_value=dict(type="int"),
            segmentation_rule_id=dict(type="int"),
            target_segmentation_rule_id=dict(type="int"),
            android=dict(type="dict"),
            state=dict(type="str", default="present", choices=["absent", "present"]),
        ),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    _memsource = get_memsource_client(module.params)
    _action = get_action(module.params)
    _result = {}
    import_settings = {}

    if _action == "create":
        file_import_settings = {}
        for param in module.params:
            if param not in ["uid", "state", "name", "file_format_configuraton"]:
                if module.params.get(param) is not None:
                    _param_split = param.split("_")
                    _param = _param_split[0] + "".join(
                        x.title() for x in _param_split[1:]
                    )
                    file_import_settings.update({_param: module.params.get(param)})

        file_import_settings.update(
            {
                module.params.get("file_format"): module.params.get(
                    "file_format_configuration"
                )
            }
        )

        import_settings = _memsource.create_import_settings(
            module.params.get("name"), file_import_settings
        )
        _result.update({"changed": True})
    elif _action == "read":
        import_settings = _memsource.get_import_settings_by_id(module.params["uid"])
    elif _action == "update":
        pass
    else:
        res = _memsource.delete_import_settings(
            module.params["uid"], do_not_fail_on_404=True,
        )
        if res.status_code == 204:
            _result.update({"changed": True})

    _result.update({"import_settings": import_settings})

    module.exit_json(**_result)


if __name__ == "__main__":
    main()
