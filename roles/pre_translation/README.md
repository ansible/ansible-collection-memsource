Pre Translation Role
=========

The pre_translation role is used to push extracted string from GitHub project to Memsource client for it to be translated to several other languages.

Requirements
------------

Applicable variables needs to be provided for the pre_translation script.

Role Variables
--------------

Below are mandatory variables required.
- email
- github_username
- github_token
- translation_supported_langs (Default - can be overridden)
- upstream_repo_url
- repo_branch
- project_name
- preTranslate (Optional: Certain translations will be pre_translated from cached memsource database, until stated false)
- project_template (Required: Project template dedicated for the specfic project to be translated)
- memsource_username (To be provided from command-line)
- memsource_password (To be provided from command-line)

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
        - "vars/push_vars.yml"
      roles:
        - role: community.memsource.pre_translation

Execution Steps
---------------

Ansible Playbook (push.yml) will be used to run this role.

1. Provide the required variables from command-line or from playbooks/vars/ directory (common.yml & push_vars.yml)
2. Provide the memsource username and memsource password from command-line
3. From the root path of the collection, run the below command

```ansible-playbook playbooks/push.yml -e memsource_username=$MEMSOURCE_USERNAME -e memsource_password=$MEMSOURCE_PASSWORD```

4. Extracted strings will be uploaded to memsource cloud.

License
-------

Apache-2.0

Author Information
------------------
- Aditya Mulik (aditya.mulik@gmail.com)
