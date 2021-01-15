#!/usr/bin/env python


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = '''
module: memsource_template_info
short_description: Gather information about templates available in Memsource.
version_added: 0.0.1
description:
    - Gather information about templates available in Memsource
author: 'Yanis Guenane (@Spredzy)'
options:
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
'''

EXAMPLES = '''
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather information about all available templates
  community.memsource.memsource_template_info:

- name: Gather information about a named template
  community.memsource.memsource_template_info:
    filters:
      name: my-memsource-template
'''

RETURN = '''
templates:
    returned: on success
    description: >
        Memsource templates that match the provided filters. Each element consists of a dict with all the information
        related to that template.
    type: list
'''

from memsource import Memsource

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.memsource.plugins.module_utils.memsource import get_default_argspec, get_memsource_client


def main():
    argument_spec = get_default_argspec()
    argument_spec = dict(
        filters=dict(default={}, type='dict')
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    _memsource = get_memsource_client(module.params)

    if module.params['filters'].get('name'):
        templates = [_memsource.get_template_by_name(module.params['filters']['name'])]
    else:
        templates = _memsource.get_templates()

    module.exit_json(templates=templates)


if __name__ == '__main__':
    main()
