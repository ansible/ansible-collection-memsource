Pre Translation Role
=========

The pre_translation role is used to push extracted string from GitHub project to Memsource client for it to be translated to several other languages.

Requirements
------------

1. pre_translation.sh | The script should be available in the upstream GitHub Repository (e.g. path: /tools/scripts/l18n/pre_translation.sh)

Role Variables
--------------

Below are mandatory variables required.
- email - (Type: str)
- github_username - (Type: str)
- github_token - (Type: str)
- translation_supported_langs (Default - can be overridden) - (Type: list)
- upstream_repo_url - (Type: str)
- repo_branch - (Type: str)
- project_name - (Type: str)
- preTranslate (Optional: Certain translations will be pre_translated from cached memsource database, until stated false) - (Type: bool)
- project_template (Required: Project template dedicated for the specfic project to be translated) - (Type: int)
- memsource_username (To be provided from command-line) - (Type: str)
- memsource_password (To be provided from command-line) - (Type: str)

Dependencies
------------

No applicable dependencies.

Playbook
----------------

The playbook push.yml is available under playbooks/ directory will be used to run the role:

    ---
    - name: Generic Localization - Pre-translation
      hosts: localhost
      vars_files:
        - "vars/common.yml"
      roles:
        - role: ansible.memsource.pre_translation

Execution Steps
---------------

Ansible Playbook (push.yml) will be used to run this role.

1. Provide the required variables from command-line as per below example \
   ```ansible-playbook playbooks/push.yml -e memsource_username=$MEMSOURCE_USERNAME -e memsource_password=$MEMSOURCE_PASSWORD -e upstream_repo_url="test_repo/prod" -e repo_branch="devel" -e project_name="Memsource Test Project" -e preTranslae=false -e project_template=310943``` \
   or \
   Another way of providing vars using command-line can be using a separate yml file (e.g. extra_vars.yml) \
   ```ansible-playbook playbooks/push.yml -e @extra_vars.yml```

2. Extracted strings will be uploaded to memsource cloud.

License
-------

Apache-2.0

Author Information
------------------
- Aditya Mulik (aditya.mulik@gmail.com)
