Post Translation Role
=========

The post_translation role is used to pull translated strings from Memsource client for the specified languages, commit, and push those strings back to the code repository.

Requirements
------------

1. GitHub CLI (<https://cli.github.com/>) | GitHub CLI needs to be installed on the machine running the role for creating a pull request
2. post_translation.sh | The script should be available in both the upstream/downstream GitHub Repository (e.g. path: /tools/scripts/l18n/post_translation.sh)

Role Variables
--------------

Below are mandatory variables required.
- translation_supported_langs (Default - can be overridden) - (Type: list)
- memsource_username (To be provided from command-line or can be set in environment variables) - (Type: str)
- memsource_password (To be provided from command-line or can be set in environment variables) - (Type: str)
- email - (Type: str)
- github_username - (Type: str)
- github_token - (Type: str)
- upstream_repo_url - (Type: str)
- downstream_repo_url - (Type: str)
- repo_branch - (Type: str)
- project_name - (Type: str)
- project_uid - (Optional) - (Type: int)

Dependencies
------------

The pre_translation role should already be executed for the latest strings to be translated and be available on Memsource client for post_translation script to work.

Playbook
----------------

The playbook pull.yml is available under playbooks/ directory will be used to run the role:

    ---
    - name: Generic Localization - Post-translation
      hosts: localhost
      vars_files:
        - "vars/common.yml"
      roles:
        - role: ansible.memsource.post_translation

Execution Steps
---------------

Ansible Playbook (pull.yml) will be used to run this role.

1. Provide the required variables from command-line as per below example \
    ```ansible-playbook playbooks/pull.yml -e memsource_username=$MEMSOURCE_USERNAME -e memsource_password=$MEMSOURCE_PASSWORD -e email="test@abc.com" -e upstream_repo_url="test_repo/prod" -e repo_branch="devel" -e downstream_repo_url="test_repo/test" -e project_name="MEMSOURCE TRANSLATION PROJECT V2.1"``` \
    or \
    Another way of providing vars using command-line can be using a separate yml file (e.g. extra_vars.yml, template is available on root path) \
    ```ansible-playbook playbooks/pull.yml -e @extra_vars.yml```

2. A pull request will be generated in the upstream repository for merging the translated strings

License
-------

Apache-2.0

Author Information
------------------
- Aditya Mulik (aditya.mulik@gmail.com)
