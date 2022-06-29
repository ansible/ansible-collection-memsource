Post Translation Role
=========

The post_translation role is used to pull translated strings from Memsource client for the specified languages, commit, and push those strings back to the code repository.

Requirements
------------

1. GitHub CLI (<https://cli.github.com/>) | GitHub CLI needs to be installed on the machine running the role for creating a pull request
2. post_translation.sh | The script should be available in the GitHub Repository (e.g. path: /tools/scripts/l18n/post_translation.sh)

Role Variables
--------------

Below are mandatory variables required.
- memsource_username (To be provided from command-line or can be set in environment variables) - (Type: str)
- memsource_password (To be provided from command-line or can be set in environment variables) - (Type: str)
- github_username - (Type: str)
- repo_url - (Type: str)
- repo_branch - (Type: str)
- fork_repo_url - (Type: str) (Please note, a fork of the main repository URL should already be present for the github_username specified)
- translation_supported_langs (Default - can be overridden) - (Type: list)
- project_name - (Type: str) (Optional: Either pass project_name or project_uid)
- project_uid - (Type: int) (Optional) - (WARNING: Do not include in pre_translation role as it will
fail)
- github_token - (Type: str) (Optional: GitHub Authentication can be done using SSH)

Dependencies
------------

The pre_translation role should already be executed for the latest strings to be translated and be available on Memsource client for post_translation script to work.
Global vars are declarared in the root folder as global_vars/all which can be overridden by passing vars from command-line.

Playbook
----------------

The playbook pull.yml is available under playbooks/ directory will be used to run the role:

    ---
    - name: Generic Localization - Post-translation
      hosts: localhost
      roles:
        - role: ansible.memsource.post_translation

Execution Steps
---------------

Ansible Playbook (pull.yml) will be used to run this role.

1. Provide the required variables from command-line as per below example \
    ```ansible-playbook playbooks/pull.yml -e memsource_username=$MEMSOURCE_USERNAME -e memsource_password=$MEMSOURCE_PASSWORD -e repo_url="test_repo/prod" -e repo_branch="devel" -e repo_url="test_repo/test" -e project_name="MEMSOURCE TRANSLATION PROJECT V2.1"``` \
    or \
    Another way of providing vars using command-line can be using a separate yml file (e.g. extra_vars.yml, template is available on root path) \
    ```ansible-playbook playbooks/pull.yml -e @extra_vars.yml```

2. A pull request will be generated in the repository for merging the translated strings

License
-------

Apache-2.0

Author Information
------------------
- Aditya Mulik (aditya.mulik@gmail.com)
